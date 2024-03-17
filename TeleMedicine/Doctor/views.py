from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from Doctor.models import *
from django.contrib.auth import authenticate,login,logout
from datetime import date
from googlesearch import search
import requests
from bs4 import BeautifulSoup


def doctorlogin(request):
    error=""
    if request.method=='POST':
        u=request.POST['emailid']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        
        try:
            if user:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'
    d={'error':error}
    return render(request,'doctorlogin.html',d)

def doctorsignup(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        con=request.POST['contact']
        email=request.POST['emailid']
        pwd=request.POST['pwd']
        specialty=request.POST['specialty']
        hospital=request.POST['hospital']
        exe=request.POST['exe']
        design=request.POST['design']
        
        user=User.objects.create_user(username=email,password=pwd,first_name=f,last_name=l)
        Doctor.objects.create(user=user,first_name=f,last_name=l,contact_no=con,experience_years=exe,hospital=hospital,email=email,designation=design,specialty=specialty)
        error="no"
        redirect('doctorlogin')
        # error='yes'
    d={'error':error}
    return render(request,'doctorsignup.html',d)

def doctorhome(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    recent_articles = Article.objects.order_by('-publish_date')  # Retrieve 5 most recent articles
    return render(request, 'doctorhome.html', {'recent_articles': recent_articles})

def createart(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    error=""
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        author=Doctor.objects.filter(email=request.user.username).first()
        print(author)
        # try:
        Article.objects.create(title=title,content=content,author=author)
        error='no'
        # except:
        #     error='yes'
    d={'error':error}
    return render(request,'createart.html',d)

def doctoredit(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Doctor.objects.get(user=user)
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['con']
        exe=request.POST['exe']
        specialty=request.POST['specialty']
        design=request.POST['design']
        hospital=request.POST['hospital']
        user.first_name=f
        user.last_name=l
        data.contact_no=c
        data.designation=design
        data.hospital=hospital
        data.specialty=specialty
        data.experience_years=exe
        user.save()
        data.save()
        error=True
    d={'data':data,'user':user,'error':error}
    return render(request,'doctoredit.html',d)

def doctorprofile(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Doctor.objects.get(user=user)
    d={'data':data,'user':user}
    return render(request,'doctorprofile.html',d)

def cpass(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    if request.POST:
        old=request.POST['old']
        new=request.POST['new']
        confirm=request.POST['confirm']
        if confirm==new:
            u=User.objects.get(username__exact=request.user.username)
            u.set_password(new)
            u.save()
            error='no'
        else:
            error='yes'
    d={'error':error}
    return render(request,'pass.html',d)

def appoint(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Doctor.objects.get(user=user)
    notes=Appointment.objects.filter(doctor=data)
    d={'notes':notes}
    return render(request,'appoint.html',d)

def deleteapp(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    notes=Appointment.objects.get(id=pid)
    notes.delete()
    return redirect('appoint')

def status(request,pid):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')
    notes=Appointment.objects.get(id=pid)
    error=""
    try:
        if request.method=='POST':
            b=request.POST['status']
            notes.status=b
            error='no'
            notes.save()
    except:
        error='yes'
    d={'error':error,'notes':notes}
    return render(request,'status.html',d)

