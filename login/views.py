from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm
from login.utLogin import CheckUserExist
class LoginView(View):
    template_name = 'login.html'
    template_homeName=''
    form_class=LoginForm
    def get(self , request,*args,**kwargs):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        error=""
        if form.is_valid() and form.email.contains("@") and form.email.constains(".com"):
            user=CheckUserExist(**form.cleaned_data)
            if not user:
                form=self.form_class()
                error="Wrong email or password."
            else:
                request.session['has_login']={'userType':user[0].userType,'pkUser':user[0].pk,'email':user[0].email,'password':user[0].password}
                return HttpResponseRedirect(reverse('panels:HomePage'))
        else:
            form=self.form_class()
        return render(request, self.template_name, {'form': form,'error':error})
