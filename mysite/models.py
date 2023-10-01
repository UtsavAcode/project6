from asyncio import format_helpers
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup (models.Model):
    user_name = models.CharField("username",max_length=50)
    email = models.EmailField("email", max_length=50)
    phone = models.IntegerField("phone")
    password = models.CharField("password",max_length=20)
    

# Profile

class Profile (models.Model):
    image = models.ImageField(default='default_image.jpg',upload_to="image")
    full_name = models.CharField("fullname", max_length=30)
    gender = models.CharField("gender",max_length=50)
    age = models.IntegerField("age")
    phone = models.IntegerField("phone")
    currentL = models.CharField("clocation",max_length=50)
    occupation = models.CharField("occupation", max_length=50)
    smoking = models.CharField("smoking",max_length=50)
    pets = models.CharField("pets", max_length=50)
    budget= models.IntegerField("budget")
    social = models.CharField("social",max_length=50)
    description =models.CharField("description",default='',max_length=70)
    

    # def image(self):
    #     return format_html('<img src="/media/{}" height=30 width=30 style="border-radius:50%">'.format(self.image_name))