from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from . models import Signup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register
from .forms import Login
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
                return redirect("/home/")
            else:
                return redirect('/')
                # messages.info(request,'username incorrect')

    
    return render(request,'forms/signin.html')


def home(request):
    return render(request,'main/home.html')



# deleting the rows: 

def delete_item(request):
    if request.method=='POST':
        item_id = request.POST.get('item_id')
        
        # Assuming you have a model named 'Item' and want to delete it
        try:
            item = Signup.objects.get(pk=item_id)
            item.delete()
            return JsonResponse({'message': 'Item deleted successfully'})
        except Signup.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)