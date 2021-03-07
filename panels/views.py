from django.shortcuts import render,reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from login.utLogin import CheckUserLogin
class HomeView(View):
    def get(self , request,*args,**kwargs):
        flag=CheckUserLogin(request)
        if flag==False:
            return HttpResponseRedirect(reverse('login:LoginPage'))
        if flag=="Teacher":
            return render(request, "Home/HomeTeacher.html",{'Email':request.session['has_login']['email']})
        else:
            return render(request, "Home/HomeStudent.html",{'Email':request.session['has_login']['email']})