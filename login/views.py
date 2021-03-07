from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .forms import LoginForm
class LoginView(View):
    template_name = 'login/login.html'
    form_class=LoginForm
    def get(self , request,*args,**kwargs):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        error=""
        if form.is_valid():
            user=Person.exist(form.cleaned_data['email'],form.cleaned_data['password'],form.cleaned_data['userType'])
            print(user)
            if not user:
                form=self.form_class()
                error="Wrong email or password."
            else:
                return HttpResponseRedirect('')
        else:
            form=self.form_class()
        return render(request, self.template_name, {'form': form,'error':error})