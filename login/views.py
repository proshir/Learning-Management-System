from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
class LoginView(View):
    template_name = 'login/login.html'
    form_class=LoginForm
    def get(self , request,*args,**kwargs):
        form=self.form_class()
        print(self.form_class)
        return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        else:
            form=NameForm()
            return render(request, self.template_name, {'form': form})