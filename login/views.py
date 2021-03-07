from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import login
from .models import Student
from login.utLogin import *
class LoginView(View):
    template_name = 'login/login.html'
    template_homeName=''
    form_class=LoginForm
    def get(self , request,*args,**kwargs):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        error=""
        if form.is_valid():
            user=CheckUserExist(**form.cleaned_data)
            if not user:
                form=self.form_class()
                error="Wrong email or password."
            else:
                user=user[0]
                request.session['has_login']={'userType':user.userType,'pkUser':user.pk,'email':user.email,'password':user.password}
                return HttpResponse('Hi')
        else:
            form=self.form_class()
        return render(request, self.template_name, {'form': form,'error':error})