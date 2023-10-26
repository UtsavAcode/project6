from django import forms


class Register(forms.Form):
    user_name = forms.CharField(label="Username", max_length=20)
    email = forms.EmailField(label="Email", max_length=30)
    phone = forms.IntegerField(label="Phone")
    password = forms.CharField(label="Password")



# class Signin(forms.Form):
#     user_name = forms.CharField(label="Username",max_length=30)
#     password = forms.CharField(label="Password",max_length=20)

class Profile1(forms.Form):

    image = forms.ImageField(label="Your Profile Picture")
    full_name = forms.CharField(label="Fullname",max_length=50)
    email = forms.EmailField(label="email")
    gender = forms.CharField(label="gender",max_length=6)
    age = forms.IntegerField(label="age")
    phone = forms.IntegerField(label="phone")
    currentL = forms.CharField(label="Current Location", max_length=20)
    occupation = forms.CharField(label="Occupation", max_length=20)
    smoking = forms.CharField(label="Smoking?", max_length=10)
    pets = forms.CharField(label="Pets",max_length=50)
    budget = forms.IntegerField(label="Your Budget")
    social = forms.CharField(label="Your Social Media")
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),  # Adjust rows and cols as needed
        label='About you'
    )
    
    
