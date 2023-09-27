from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from . models import Signup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register
from .forms import Login

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'components/about.html')

def details(request):
    return render(request,'components/details.html')

def contact(request):
    return render(request,'components/contact.html')

def team(request):
    return render(request,'components/team.html')

def services(request):
    return render(request,'components/services.html')


def admin(request):
    return render(request,'admin/padmin.html')

def admin_nav(request):
    return render(request,'admin/admin_nav.html')



# this is the area for the register:

def register(request):

    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            signup = Signup(user_name=form.cleaned_data['user_name'],
                            email=form.cleaned_data['email'],
                            phone=form.cleaned_data['phone'],
                            password=form.cleaned_data['password'],
                            )
            signup.save()
            return HttpResponseRedirect("/signin/")

        
    form = Register()
   
    return render(request,'forms/register.html',{
       "form":form
     })



     


# this is the area of login 

def sign(request):
    if request.method == 'POST':
        form1 = Register(request.POST)
        if form1.is_valid():
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user is not None: 
                login(request,user)
                return redirect('/home/')

        else: 
            form1 = Login()
    
    

    return render(request,'forms/signin.html')


def home(request):
    return render(request,'main/home.html')