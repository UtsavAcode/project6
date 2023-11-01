
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup (models.Model):
    username = models.CharField("username",max_length=50)
    email = models.EmailField("email",unique=True)
    phone = models.IntegerField("phone")
    password = models.CharField("password",max_length=20)
    

# Profile

class Profile (models.Model):
    
    image = models.ImageField(default='default_image.jpg',upload_to="image")
    username = models.CharField("username", max_length=30)
    email = models.EmailField("email")
    gender = models.CharField("gender",max_length=50)
    age = models.IntegerField("age")
    phone = models.IntegerField("phone")
    currentL = models.CharField("currentL",max_length=50)
    occupation = models.CharField("occupation", max_length=50)
    smoking = models.CharField("smoking",max_length=50)
    pets = models.CharField("pets", max_length=50)
    budget= models.IntegerField("budget")
    social = models.CharField("social",max_length=50)
    description =models.CharField("description",default='',max_length=70)
    

#    connections



class ConnectionRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user.username} to {self.to_user.username}"


class Chat(models.Model):
    users = models.ManyToManyField(User)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



class ChatMessage(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
