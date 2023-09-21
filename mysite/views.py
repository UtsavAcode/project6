from django.shortcuts import render
from django.template .loader import render_to_string
from django.http import HttpResponse


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

def sign(request):
    return render(request,'forms/signin.html')

def admin(request):
    return render(request,'admin/padmin.html')

def admin_nav(request):
    return render(request,'admin/admin_nav.html')

