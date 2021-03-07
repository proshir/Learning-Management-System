from django.forms import ModelForm
from django import forms
from .models import Person,Types
class LoginForm(ModelForm):
    class Meta:
        model = Person
        labels = {'email': 'Email:','password': 'Password','userType':'Type:'}
        fields= ['email', 'password','userType']
        widgets = {
            'password': forms.PasswordInput() ,
            'userType': forms.RadioSelect(choices=Types)
            }
