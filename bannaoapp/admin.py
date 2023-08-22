from django.contrib import admin
from bannaoapp.models import Orders 
from django.contrib.admin.sites import site
# Register your models here.
class OrdersScetion(admin.ModelAdmin):
    list_display = ('orderedBy','status', 'file' ,'volume','weight','calculatedPrice','description')
    
admin.site.register(Orders,OrdersScetion)
