"""
URL configuration for TeleMedicine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Doctor.views import *
from Patient.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('userlogin',userlogin,name='userlogin'),
    path('signup',signup1,name='signup'),
    path('profile',profile,name='profile'),
    path('Logout',Logout,name='Logout'),
    path('editprofile',editprofile,name='editprofile'),
    path('changepass',changepass,name='changepass'),
    path('recentarticles',recentarticles,name='recentarticles'),
    path('searchdisease',searchdisease,name='searchdisease'),
    path('makeapp',makeapp,name='makeapp'),
    path('viewapp',viewapp,name='viewapp'),
    path('doctorlogin',doctorlogin,name='doctorlogin'),
    path('doctorsignup',doctorsignup,name='doctorsignup'),
    path('doctorhome',doctorhome,name='doctorhome'),
    path('createart',createart,name='createart'),
    path('doctoredit',doctoredit,name='doctoredit'),
    path('doctorprofile',doctorprofile,name='doctorprofile'),
    path('cpass',cpass,name='cpass'),
    path('appoint',appoint,name='appoint'),
    path('deleteapp/<int:pid>',deleteapp,name='deleteapp'),
    path('status/<int:pid>',status,name='status'),
    path('deleteapp2/<int:pid>',deleteapp2,name='deleteapp2'),
    path('doctorsprofile',doctorprofile,name='doctorsprofile'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
]

