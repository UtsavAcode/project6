
from django.db import models
from django.contrib.auth.models import User
import datetime,os
# Create your models here.
class Signup (models.Model):
    username = models.CharField("username",max_length=50)
    email = models.EmailField("email",unique=True)
    phone = models.IntegerField("phone")
    password = models.CharField("password",max_length=20)
    registration_date = models.DateTimeField("registration date", auto_now_add=True)








# Profile
def filepath(request,filename):
    old_filename = filename
    time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s"%(time_now,old_filename)
    return os.path.join('profiles/',filename)

class Profile (models.Model):
    # Other fields in your Profile model
    image = models.ImageField(default='default_image.jpg',upload_to=filepath)
    username = models.CharField("username", max_length=30)
    email = models.EmailField("email")
    gender = models.CharField("gender",max_length=50)
    age = models.IntegerField("age",default=18)
    phone = models.IntegerField("phone")
    password = models.CharField("password",max_length=250)
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6, null=True, blank=True)

    currentL = models.CharField("currentL",max_length=50)
    occupation = models.CharField("occupation", max_length=50)
    smoking = models.CharField("smoking",max_length=50)
    pets = models.CharField("pets", max_length=50)
    budget= models.IntegerField("budget",default=1000)
    social = models.CharField("social",max_length=50)
    description =models.CharField("description",default='',max_length=70)
    registration_date = models.DateTimeField(verbose_name="Date Registered",auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.username
    
    
    
# chatting 




   