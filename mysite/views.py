from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from . models import Signup
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register
from .forms import Profile1
from django.http import request

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
    objs = Signup.objects.all()
    return render(request,'admin/padmin.html',{'objs':objs})

def admin_nav(request):
    return render(request,'admin/admin_nav.html')

def register_table(request):
    objs = Signup.objects.all()
    return render(request,'admin/register_table.html',{'objs':objs})

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('/padmin/')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists ():
            # messages.info(request, 'Account not found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
        user_obj = authenticate(username=username, password=password)

        if user_obj and user_obj.is_superuser:
            login(request, user_obj)
            return redirect('/padmin/')
            
        # messages.info(request, 'Invalid password')
        return redirect('/')
          
    return render(request,'forms/admin_login.html')



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
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request,user)
                return redirect("/dash/")
            else:
                return redirect('/')
                # messages.info(request,'username incorrect')

    
    return render(request,'forms/signin.html')










def profile1(request):
    
    if request.method == "POST":
        form = Profile1(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile (
                image = request.FILES['image'],
                 #form.cleaned_data['image'],
                full_name = form.cleaned_data['full_name'],
                gender = form.cleaned_data['gender'],
                age = form.cleaned_data['age'],
                phone = form.cleaned_data['phone'],
                currentL = form.cleaned_data['currentL'],
                occupation = form.cleaned_data['occupation'],
                smoking = form.cleaned_data['smoking'],
                pets = form.cleaned_data['pets'],
                budget = form.cleaned_data['budget'],
                social = form.cleaned_data['social'],
                description = form.cleaned_data['description'],
                
                
            )

            profile.save()
            return HttpResponseRedirect('/dash/')
    form = Profile1()


    return render(request, 'forms/profile1.html',{
       "form":form
     })


def dash(request):
    objs = Profile.objects.all()
    return render(request, 'components/dash.html',{"objs":objs})