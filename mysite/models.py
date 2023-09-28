from django.db import models

# Create your models here.
class Signup (models.Model):
    user_name = models.CharField("username",max_length=50)
    email = models.EmailField("email", max_length=50)
    phone = models.IntegerField("phone")
    password = models.CharField("password",max_length=20)
    

