from django.forms import ModelForm
from django import forms
from .models import Homework
class HomeworksAddForm(ModelForm):
    class Meta:
        model = Homework
        labels = {'name': 'Name:','desctiption': 'Description:','deadline':'Deadline:'}
        fields= ['name', 'description','deadline']