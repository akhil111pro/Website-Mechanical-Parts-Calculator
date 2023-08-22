from django.shortcuts import render
from django.core.files.storage import FileSystemStorage 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, OrderForm
from .models import *

import numpy as np
from stl import mesh

# akhil pass - 1234rocks


def landing(request):
    return render(request, 'landing.html')


def upload(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    context = {'form': form, 'update': Orders}

    if request.method == 'POST':
        if form.is_valid():

            im = form.cleaned_data['file']
            des = form.cleaned_data['description']
            
            file = request.FILES['file']
            
            file_content = file.temporary_file_path()
            
            print(file_content)
            your_mesh = mesh.Mesh.from_file(file_content)
           
            volume, cog, inertia = your_mesh.get_mass_properties()
            Vol = format(volume)
            calVol = int(float(Vol))
            print(Vol)
            calWeight = float(Vol) * float(0.00124)
            calPrice = calWeight * int(5)

            ame = Orders(file=im, description=des, orderedBy=request.user.username,
                         weight=calWeight, volume=calVol, calculatedPrice=calPrice)

            ame.save()

            messages.success(request, 'File Uploaded')
        else:
            messages.success(request, 'File Upload Failed')

        return redirect('userDashboard')
    return render(request, 'upload.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Regestration complete')
            return redirect('user_login')
    else:
        form = SignUpForm()
        messages.info(request, 'username or password is incorrect')
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userDashboard')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'user_login.html', context)


def userDashboard(request):
    orders = Orders.objects.filter(orderedBy=request.user.username)

    return render(request, 'userDashboard.html', {'orders': orders})


def test(request):

    return render(request, 'landing.html')
