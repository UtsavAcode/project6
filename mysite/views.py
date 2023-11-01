from django.shortcuts import render, redirect 
from django.template .loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from . models import Signup
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from .forms import Register
# from .forms import Signin
# from .forms import Profile1
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
from .models import ConnectionRequest

# all for the chatting section
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ChatMessage












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

        email_exists = Signup.objects.filter(email = normalized_email).exists()
        phone_exists = Signup.objects.filter(phone = phone).exists()

        if email_exists:
            messages.error(request,"Email is taken")
        
        if phone_exists:
            messages.error(request,"Phone is taken")

        if email_exists or phone_exists:
            
            return redirect(request,'/register/')
        
        else:
            user = Signup(username = username, email = normalized_email, phone = phone, password = hashed_password) 

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
            user = Signup.objects.get(email = normalized_email)
            password_matched = check_password(password,user.password)
            
            if password_matched:
                request.session['email'] = normalized_email
                return redirect('/dash/')
            else:
                messages.error(request,"Incorrect Password")
                return redirect('/signin/')
            
        except Signup.DoesNotExist as e:
            print(e)
            messages.error(request,"Account doesnot exists.")
            return redirect('/register/')
    return render(request,'forms/signin.html')



# new profile creation 









# User Profile creation 
def profile1(request):  
    if request.method == 'POST':
        # Retrieve form data from the request
        image = request.FILES['image']
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

        # Create a new Profile instance with the form data
        profile = Profile(
            image=image,
            username=username,
            email=email,
            gender=gender,
            age=age,
            phone=phone,
            currentL=currentL,
            occupation=occupation,
            smoking=smoking,
            pets=pets,
            budget=budget,
            social=social,
            description=description
        )

        # Save the Profile instance to the database
        profile.save()

        # Redirect to a success page or wherever you'd like
        return redirect('/dash/')

    return render(request, 'forms/profile1.html')  
        


        # email = request.session.get('email',None)
        # if email:
        #     user = Signup.objects.get(email = email)

        #     if request.method =='POST':
        #         if 'image' in request.FILES:
        #             if user.user_profile:
        #                 default_storage.delete(user.user_profile.path)
                    
        #             image =  request.FILES['image']
        #             user.user_profile.save(image.name,image)

        #             username = request.POST.get('username')
        #             email = request.POST.get('email')
        #             gender = request.POST.get('gender')
        #             age = request.POST.get('age')
        #             phone = request.POST.get('phone')
        #             location = request.POST.get('location')
        #             occupation = request.POST.get('occupation')
        #             social = request.POST.get('social')
        #             budget = request.POST.get('budget')
        #             pets =  request.POST.get('pets')
        #             smoking =  request.POST.get('smoking')
        #             description = request.POST.get('description')

        #             normalized_email = email.lower()

        #             user.username = username
        #             user.email =  email
        #             user.phone = phone
                    
        #             try:
        #                 user.save()
        #                 messages.info(request,"Profile successfully updated.")
        #             except Exception as e:
        #                 print("Exception")

        #             data = user
        #             return render(request, 'forms/profile1.html',{'data':data})
        #     else:
        #         messages.error(request,"Sessio Expired. Please login again.")
        #         return redirect('/login/')


        
        
    

  
    


    




@login_required
def dash(request):
    user_id = request.user.id
    objs = Profile.objects.all()
    return render(request, 'main/dash.html', {"objs": objs, 'user_id': user_id})






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

        return redirect('/register_table')









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
    



# the chatting section



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Chat, ChatMessage
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q

@login_required
def create_chat(request, to_user_id):
    from_user = request.user
    to_user = get_object_or_404(User, id=to_user_id)

    # Check if a chat between these two users already exists
    chat = Chat.objects.filter(Q(users=from_user) & Q(users=to_user))

    if chat.exists():
        chat = chat[0]
    else:
        # Create a new chat conversation
        chat = Chat.objects.create()
        chat.users.add(from_user, to_user)

    return JsonResponse({"chat_id": chat.id})

@login_required
@require_POST
def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    sender = request.user.profile
    content = request.POST.get("content")

    if content:
        message = ChatMessage(sender=sender, receiver=chat.users.exclude(id=sender.id).first(), message=content)
        message.save()

    return JsonResponse({"message_id": message.id})

@login_required
def get_chat_history(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = chat.chatmessage_set.all()
    chat_history = [{"sender": message.sender.username, "message": message.message, "timestamp": message.timestamp} for message in messages]

    return JsonResponse({"chat_history": chat_history})
