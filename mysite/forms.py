from django import forms


class Register(forms.Form):
    user_name = forms.CharField(label="Username", max_length=20)
    
    email = forms.EmailField(label="Email", max_length=30)
    phone = forms.IntegerField(label="Phone")
    password = forms.CharField(label="Password")
    

class Login(forms.Form):
    email = forms.CharField(label="Email")
    password = forms.CharField(label="Password")
    