from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as Logout
from .models import *
from .forms import UserForm



global name 

# Create your views

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("pas1")
        pass2=request.POST.get("pas2")
        if pass1==pass2:
            try:
              myusers=User.objects.create_user(username,email,pass1)
              myusers.last_name=" "
              myusers.first_name=" "
              
              myusers.save()
              return redirect('login')
            except Exception as e:
                message='''
                Your have already registered...
                Please try to login 
                ''' 
                return render(request,'html/register.html',{'message':message})
            
        else:
            message="Please check if you entered details is correct"
            return render(request,'html/register.html',{'message':message})
    return render(request,'html/register.html')


def logout(request):
    Logout(request)
    return redirect('login')

    
def Error404(request,exception):
    return render(request,'html/404error.html')


def login(request):
    global name 
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(username=username,password=pass1)
        
        if user is not None:
            Login(request,user)
            name=str(username)  
            return redirect('home',i=name)
        else:
            message='Please enter valid details'
            return render(request,'html/login.html',{'message':message})
    return render(request,'html/login.html')


@login_required
def home(request,i):
    import datetime
    return render(request,'html/home.html',{'i':i,'date':str(datetime.datetime.now())[0:4]})

@login_required
def fileupload(request,i):
    if request.method=="POST":
        fname=request.POST.get('name')
        fi=request.FILES['file']
        obj=UserFile.objects.create(name=fname,file=fi)
        obj.save()
        return render(request,'html/fileupload.html',{'n':fname,'form':UserForm,'m':"File uploaded sucessfully"})
    return render(request,'html/fileupload.html',{'n':i,'form':UserForm})

@login_required
def delete(request,i):
    
    import os 
    delobj=UserFile.objects.get(id=int(i))
    n=UserFile.objects.get(id=int(i)).name
    f=str(UserFile.objects.get(id=int(i)).file)
    obj=UserFile.objects.filter(name=n)
    delobj.delete()
    import os 
    os.remove(f)
    return render(request,'html/seefile.html',{'data':obj,'j':n,'m':"File deleted"})

@login_required
def seefile(request,i):
    obj=UserFile.objects.filter(name=i)
    
    return render(request,'html/seefile.html',{'data':obj,'j':i})

def For(request):
    return render(request,'html/forgot-password.html')

