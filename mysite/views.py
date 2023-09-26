from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from . models import Signup
from .models import Login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def home(request):
    return render(request,'main/home.html')

# this is the area for the register:

def register(request):
    if request.method == "POST":
        user_name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        date = request.POST['date']

        new_sign = Signup(user_name = user_name,
                          email = email,
                          phone = phone,
                          password = password,
                          date = date,
                          )

        new_sign.save()
        return HttpResponseRedirect("/sign")
    
        if user_name == "":
            return render(request,"forms/register.html",{
                "has_error: True"
            })

    return render(request,'forms/register.html',{
        "has_error": False
    })


# this is the area of login 

def sign(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None: 
            login(request, user)
            return redirect("/about")
    
        else:
            messages.success(request,("There was an error"))
            return redirect("/sign")


    return render(request,'forms/signin.html')