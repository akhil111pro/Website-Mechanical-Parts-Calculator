from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('upload',views.upload , name = 'upload' ),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login , name = 'user_login'),
    path('userDashboard', views.userDashboard , name='userDashboard'),
    path('test',views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)