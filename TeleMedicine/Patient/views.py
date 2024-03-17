from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from Doctor.models import *
from django.contrib.auth import authenticate,login,logout
from datetime import date
from googlesearch import search
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request,'index.html') 

def userlogin(request):
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
    return render(request,'login.html',d)

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

def signup1(request):
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        con=request.POST['contact']
        email=request.POST['emailid']
        pwd=request.POST['pwd']
        age=request.POST['age']
        occupation=request.POST['occupation']
        
        user=User.objects.create_user(username=email,password=pwd,first_name=f,last_name=l)
        Patient.objects.create(user=user,Firstname=f,Lastname=l,contactno=con,age=age,occupation=occupation,email=email)
        error="no"
    d={'error':error}
    return render(request,'signup.html',d)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Patient.objects.get(user=user)
    d={'data':data,'user':user}
    return render(request,'profile.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Patient.objects.get(user=user)
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        c=request.POST['con']
        age=request.POST['age']
        occupation=request.POST['occupation']
        user.first_name=f
        user.last_name=l
        data.contactno=c
        data.age=age
        data.occupation=occupation
        user.save()
        data.save()
        error=True
    d={'data':data,'user':user,'error':error}
    return render(request,'editprofile.html',d)

def changepass(request):
    error=""
    if not request.user.is_authenticated:
        return redirect('userlogin')
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
    return render(request,'changepass.html',d)

def recentarticles(request):
    recent_articles = Article.objects.order_by('-publish_date')[:20]  # Retrieve 5 most recent articles
    return render(request, 'recentarticles.html', {'recent_articles': recent_articles})

def searchdisease(request):
    if request.method == 'POST':
        query = request.POST['sea']
        search_results = search(query)
        if search_results:
            # Get the content of the first search result
            first_result = next(iter(search_results), None)
            if first_result:
                response = requests.get(first_result)
                if response.status_code == 200:
                    content = response.text
                    # Extract relevant information from the HTML content using BeautifulSoup
                    soup = BeautifulSoup(content, 'html.parser')
                    paragraphs = soup.find_all('p')
                    search_results = [p.get_text() for p in paragraphs]
                else:
                    search_results = ['Failed to fetch search results.']
            else:
                search_results = ['No search results found.']
        else:
            search_results = ['No search results found.']
        return render(request, 'searchdisease.html', {'query': query, 'search_results': search_results})
    else:
        return render(request, 'searchdisease.html')

def makeapp(request):
    doctors = Doctor.objects.all()
    error=""
    if request.method=='POST':
        date=request.POST['date']
        time=request.POST['time']
        reason=request.POST['reason']
        patient=User.objects.filter(username=request.user.username).first()
        doctor=request.POST['doc']
        user = User.objects.get(username=doctor)
        doctor1 = Doctor.objects.get(user=user)
        error=""
        try:
            appointment = Appointment.objects.create(
                    doctor=doctor1,  # Set doctor to None for now
                    patient=patient,
                    appointment_date=date,
                    appointment_time=time,
                    reason_for_visit=reason,
                    status='Pending'
            )
            error='no'
        except:
            error='yes'
    d={'doctors':doctors,'error':error}
    return render(request,'makeapp.html',d)

def viewapp(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error=False
    user=User.objects.get(id=request.user.id)
    data=Appointment.objects.filter(patient=user)
    d={'data':data}
    return render(request,'viewapp.html',d)

def deleteapp2(request,pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes=Appointment.objects.get(id=pid)
    notes.delete()
    return redirect('viewapp')

def doctorprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    doctor=Doctor.objects.all()
    d={'doctor':doctor}
    return render(request,'doctorsprofile.html',d)
def about(request):
    return  render(request,'about.html')

def contact(request):
    return  render(request,'contact.html')