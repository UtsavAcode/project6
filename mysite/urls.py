from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index',),
    path('about/',views.about, name='about'),
    path('details/',views.details, name='details'),
    path('contact/',views.contact, name='contact'),
    path('services/', views.services,name='services'),
    path('compteam/',views.team,name='team'),
    path('register/',views.register,name='register'),
    path('signin/',views.sign,name='sign'),
    path('padmin/',views.admin, name='padmin'),
    path('admin_nav/',views.admin_nav, name='admin_nav'),
    
    path('admin_login/',views.admin_login, name='admin_login'),
    path('register_table/',views.register_table, name='register_table'),
    path('profile1/',views.profile1, name='profile1'),
    path('dash/', views.dash, name="dash"),
    path('user_detail/', views.user_detail, name="user_detail"),
    path('find_roommates/', views.find_roommates, name='find_roommates')
    
    
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
