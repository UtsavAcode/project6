from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . models import Signup
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Register
# from .forms import Signin
from .forms import Profile1
from django.http import request
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

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
        name= request.POST.get('user_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        normalized_email = email.lower()
        hashed_password = make_password(password)

        email_exists = Signup.objects.filter(email = normalized_email).exists()
        phone_exists = Signup.objects.filter(phone = phone).exists()

        if email_exists:
            messages.error(request,"Email is taken")
        
        if phone_exists:
            messages.error(request,"Phone is taken")

        if email_exists or phone_exists:
            
            return redirect(request,'/register/')
        
        else:
            user = Signup(user_name = name, email = normalized_email, phone = phone, password = hashed_password) 

            try:
                user.save()
                request.session['email'] = normalized_email
                return redirect('/signin/')
            
            except Exception as e:
                pass

    return render(request,'forms/register.html')




     


# this is the area of login 

def signin(request):
    if request.method == 'POST':    
        email = request.POST.get('email')
        password = request.POST.get('password')
        normalized_email = email.lower()

        try:
            user = Signup.objects.get(email=normalized_email)
            password_matched = check_password(password,user.password)
            
            if password_matched:
                request.session['email'] = normalized_email
                return redirect('/profile1/')
            else:
                messages.error(request,"Incorrect password")
                return redirect('/signin/')
            
        except Signup.DoesNotExist as e:
            print(e)
            messages.error(request,"Account doesnot exist")
            return redirect('/signin/')
        
   
    return render(request,'forms/signin.html')



# User Profile creation 
def profile1(request):
    
    if request.method == "POST":
        form = Profile1(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile (
                image = request.FILES['image'],
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
    
    return render(request, 'main/dash.html',{"objs":objs})

def user_detail(request):
    objs = Profile.objects.all()
    return render(request, 'main/user_detail.html',{"objs":objs})



# matching

def find_roomates(request):
    current_user = Profile.objects.latest('id')
    users = Profile.objects.exclude(id=current_user.id)


    matching_users=[]

    for user in users:
        if(
            user.budget - 500 <= current_user.budget<=user.budget + 500
            and user.currentL == current_user.currentL
            # and user.age == current_user.age
            # and abs(user.age- current_user.age)<=5
            
        ):
            matching_users.append(user)

        elif(
             
            user.smoking == current_user.smoking
        ):
            matching_users.append(user)

        num_matches = len (matching_users)
    
    return render(request, 'main/match.html',{'matching_users':matching_users,'num_matches':num_matches})


# user navigation

def user_nav(request):
    
    return render(request,'main/user_nav.html')

# Delete
def delete(request):
    return render(request, 'admin/delete.html')

# Update
def update(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        try:
            obj = Signup.objects.get(email=email)
        except Signup.DoesNotExist:
            return HttpResponse("User not found", status=404)

        return render(request, 'admin/update.html', {'obj': obj})

    elif request.method == 'POST':
        email = request.POST.get('email')
        user_name = request.POST.get('user_name')
        phone = request.POST.get('phone')

        try:
            obj = Signup.objects.get(email=email)
            obj.user_name = user_name
            obj.phone = phone
            obj.save()
        except Signup.DoesNotExist:
            return HttpResponse("User not found", status=404)

        return redirect('/register_table')









def update_profile(request):
    return render(request, 'forms/profile1.html')

def search(request):
    
    query = request.GET.get('search','')
    
    profiles = Profile.objects.all()

    if query:
        profiles = profiles.filter(
            Q(full_name__icontains=query) | Q(currentL__icontains=query) | Q(age__icontains=query) | Q(budget__icontains=query) | Q(occupation__icontains=query) | Q(gender__icontains=query))
        
    if not profiles:
        return redirect('/dash/')

    return render(request, 'main/search.html',{'profiles':profiles, 'query':query})



def delete_row(request, row_id):
    try:
        Signup.objects.get(pk=row_id).delete()
        return JsonResponse({'message': 'Deleted successfully.'}, status=200)
    except Signup.DoesNotExist:
        return JsonResponse({'message': 'Item not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'message': 'Error deleting item.'}, status=500)