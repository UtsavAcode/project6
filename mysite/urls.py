from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index',),
    path('about/',views.about, name='about'),
    path('details/',views.details, name='details'),
    path('contact/',views.contact, name='contact'),
    path('services/', views.services,name='services'),
    path('compteam/',views.team,name='team'),
    path('sign/',views.sign,name='sign'),
    path('register/',views.register,name='register'),
    path('padmin/',views.admin, name='padmin'),
    path('admin_nav/',views.admin_nav, name='admin_nav'),
    path('home/',views.home, name="home"),
    
]