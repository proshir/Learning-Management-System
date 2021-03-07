from django.forms import ModelForm
from django import forms
from .models import Person
class LoginForm(ModelForm):
    class Meta:
        model = Person
        labels = {'email': 'Email:','password': 'Password'}
        fields= ['email', 'password']
        widgets = {'password': forms.PasswordInput() }
