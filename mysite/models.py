from django.db import models

# Create your models here.
class Signup (models.Model):
    user_name = models.CharField("username",max_length=50)
    email = models.CharField("email", max_length=50)
    phone = models.IntegerField("phone", max_length=13)
    password = models.CharField("password",max_length=20)
    date = models.DateTimeField("date", max_length=8)

class Login (models.Model):
    email = models.CharField("email",max_length=50)
    password = models.CharField("password",max_length=20)