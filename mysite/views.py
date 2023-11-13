from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . models import Signup
from . models import Profile
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from .forms import Register
# from .forms import Signin
# from .forms import Profile1
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.http import request
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# matching section 
from django.db.models import F
from django.db.models import FloatField
from django.db.models import ExpressionWrapper
from django.db.models import Func
from django.db.models import Value
from django.db.models import F, FloatField, ExpressionWrapper, Value
from geopy.distance import geodesic




from io import BytesIO




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
        username= request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        normalized_email = email.lower()
        hashed_password = make_password(password)

        email_exists = Profile.objects.filter(email = normalized_email).exists()
        phone_exists = Profile.objects.filter(phone = phone).exists()

        if email_exists:
            message = "This email is taken"
        
        if phone_exists:
            message="The phone is taken."

        if email_exists or phone_exists:
            
            return redirect(request,'/register/')
        
        else:
            user = Profile(username = username, email = normalized_email, phone = phone, password = hashed_password) 

            try:
                user.save()
                request.session['email'] = normalized_email
                return redirect('/signin/')
            
            except Exception as e:
                print(f'Exception in line 132 {e}')

    
    return render(request,'forms/register.html')


















     


# this is the area of login 

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        normalized_email = email.lower()
        try:
            user = Profile.objects.get(email = normalized_email)
            password_matched = check_password(password,user.password)
            
            if password_matched:
                request.session['email'] = normalized_email
                return redirect('/dash/')
            else:
                messages.error(request,"Incorrect Password")
                return redirect('/signin/')
            
        except Profile.DoesNotExist as e:
            print(e)
            messages.error(request,"Account doesnot exists.")
            return redirect('/register/')
    return render(request,'forms/signin.html')



# new profile creation 









# User Profile creation 
def profile1(request):  
    email = request.session.get('email',None)
    print(email)
    if email:
        if request.method == 'POST':
            
            # Retrieve form data from the request
            username = request.POST['username']
            email = request.POST['email']
            gender = request.POST['gender']
            age = request.POST['age']
            phone = request.POST['phone']
            currentL = request.POST['currentL']
            occupation = request.POST['occupation']
            smoking = request.POST['smoking']
            pets = request.POST['pets']
            budget = request.POST['budget']
            social = request.POST['social']
            description = request.POST['description']
            # Add the following lines to get latitude and longitude values
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            print(latitude,longitude)
            me = Profile.objects.get(email = email)
            if 'image' in request.FILES:
                if me.image:
                    default_storage.delete(me.image.path)
                image = request.FILES['image']
                me.image.save(image.name,image)
            # Create a new Profile instance with the form data
            
            me.username=username
            me.email=email
            me.gender=gender
            me.age=age
            me.phone=phone
            me.currentL=currentL
            me.occupation=occupation
            me.smoking=smoking
            me.pets=pets
            me.budget=budget
            me.social=social
            me.description=description

            me.latitude=latitude # Store latitude
            me.longitude=longitude  # Store longitude


           
            # Save the Profile instance to the database
            try:    
                me.save()
            
            except Exception as e:
                print(e)

            

            # Redirect to a success page or wherever you'd like
            return redirect('/dash/')
        
        
        

        user = Profile.objects.get(email = email)
        context = {
            'user':user
        }
        return render(request, 'forms/profile1.html',context)
    else:
        pass
        

        
        
    

  
    


    





def dash(request):
    email = request.session.get('email',None)
    if email:

        user_id = request.user.id
        objs = Profile.objects.all()
        return render(request, 'main/dash.html', {"objs": objs, 'user_id': user_id})
    else:
        pass






def user_detail(request):
    objs = Profile.objects.all()
    return render(request, 'main/user_detail.html',{"objs":objs})






# matching

class Haversine(Func):
    function = "Haversine"
    output_field = FloatField()






def find_roomates(request):
    email = request.session.get('email',None)
    print(email)
    if email:
        me = Profile.objects.get(email = email)
        users = Profile.objects.exclude(id=me.id)

        matching_users = []
        max_distance = 10  

        for user in users:
            user_location = (user.latitude, user.longitude)
            current_user_location = (me.latitude, me.longitude)
            distance = geodesic(user_location, current_user_location).kilometers
            print(f"User: {user.username}, Distance: {distance} km")



            if distance <= max_distance:
                
                    matching_users.append(user)

        num_matches = len(matching_users)
        

        return render(request, 'main/match.html', {'matching_users': matching_users, 'num_matches': num_matches})
    else:
        pass




def print_report(request):
    email = request.session.get('email',None)
    if email:
        pass
    else:
        pass

def user_nav(request):
    if request.user.is_authenticated:
        profile_picture = request.user.profile.image.url if hasattr(request.user, 'profile') and request.user.profile.image else None
    else:
        profile_picture = None
    return render(request,'main/user_nav.html',{'profile_picture': profile_picture})

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

        return redirect('/register_table/')









def update_profile(request):
    return render(request, 'forms/profile1.html')



def search(request):
    
    query = request.GET.get('search','')
    
    profiles = Profile.objects.all()

    if query:
        profiles = profiles.filter(
            Q(username__icontains=query) | Q(currentL__icontains=query) | Q(age__icontains=query) | Q(budget__icontains=query) | Q(occupation__icontains=query) | Q(gender__icontains=query))
        
    if not profiles:
        # return redirect('/dash/')
         message = "No results found."
    
    num_matches = len(profiles)

    return render(request, 'main/search.html',{'profiles':profiles, 'query':query})





def delete_row(request, row_id):
    try:
        Signup.objects.get(pk=row_id).delete()
        return JsonResponse({'message': 'Deleted successfully.'}, status=200)
    except Signup.DoesNotExist:
        return JsonResponse({'message': 'Item not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'message': 'Error deleting item.'}, status=500)
    


def profile_view(request):
    objs = Profile.objects.all()
    
    return render(request, 'admin/profile_view.html',{'objs':objs})






# the chatting section

from django.db.models import Count
from django.shortcuts import render
from datetime import datetime

def registration_report(request):
    current_month = datetime.now().month
    registrations = Signup.objects.filter(registration_date__month=current_month)

    registration_count = registrations.count()

    return render(request, 'admin/registration_report.html', {'registration_count': registration_count})


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf_report(request):
    try:
        data = Profile.objects.all()
        context = {'data':data}
        template = get_template('admin/registration_report.html')
        html = template.render(context)
        pdf_buffer = BytesIO()
        pisa.CreatePDF(html,dest=pdf_buffer)
        pdf_buffer.seek(0)

        response = HttpResponse(pdf_buffer,content_type='application/pdf')
        response['Content-Disposition'] = f'filename="report.pdf"'
        return response
    except Exception as e:
        print(f'Exception is {e}')

from django.shortcuts import redirect, get_object_or_404

from django.contrib import messages

def delete_profile(request, profile_id):
    # Get the profile object based on the ID
    profile = get_object_or_404(Profile, id=profile_id)

    if request.method == 'POST':
        # Delete the profile
        profile.delete()
        messages.success(request, 'Profile deleted successfully.')
    else:
        messages.error(request, 'Invalid request.')

    return redirect('/profile_view/')

def sendemail(request):
    email = request.session.get('email',None)
    if email:
        if request.method == 'POST':
            connect_email = request.POST.get('email')
            user = Profile.objects.get(email = connect_email)
            me = Profile.objects.get(email = email)
            message = f'Dear {user.username}, {me.username} Wants to connects you for conversation.'

            try:
                send_mail(
                    "Connect request",
                    message,
                    "utsavadhikary457@gmail.com",
                    [connect_email],
                    fail_silently=False
                )
                messages.success(request,"Email Send Successfully.")
                return redirect('mysite:dash')
            except Exception as e:
                print(f"Exception sending email {e}")

    else:
        pass


from django.shortcuts import render
from datetime import datetime, timedelta

def generate_weekly_report(request):
    email = request.session.get('email', None)

    if email:
        try:
            me = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return render(request, 'main/error.html', {'error_message': 'Profile not found for the given email.'})

        users = Profile.objects.exclude(id=me.id)

        matching_users = []
        max_distance = 10  # You may want to make this configurable

        # Calculate the start and end dates for the week
        today = datetime.now()
        start_date = today - timedelta(days=today.weekday())
        end_date = start_date + timedelta(days=6)

        for user in users:
            distance = calculate_distance(me, user)

            if distance <= max_distance:
                matching_users.append(user)

        # Filter matching users based on their registration date within the week
        matching_users_in_week = [
            user for user in matching_users
            if start_date <= user.registration_date <= end_date
        ]

        num_matches = len(matching_users_in_week)

        return render(request, 'main/weekly_report.html', {'matching_users': matching_users_in_week, 'num_matches': num_matches})
    else:
        # Handle the case where the email session variable is not set
        return render(request, 'main/error.html', {'error_message': 'Email session variable not set.'})

        