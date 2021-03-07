from .models import Person
from django import forms
class LoginForm(forms.Form):
    class Meta:
    class Meta:
        model= Person
        fields=[
           'email',
           'password'
            ]
       widgets = {
      'password': forms.PasswordInput()
         }