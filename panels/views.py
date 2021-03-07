from django.shortcuts import render,reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
from login.utLogin import CheckUserExistReq,CheckUserLogin
from login.models import Teacher,Student
from .forms import HomeworksAddForm
from .models import Homework
class HomeView(View):
    def get(self , request,*args,**kwargs):
        flag=CheckUserLogin(request)
        if flag==False:
            return HttpResponseRedirect(reverse('login:LoginPage'))
        if flag=="Teacher":
            return render(request, "Teacher/HomeTeacher.html",{'Email':request.session['has_login']['email'],'HomeworksUrl':reverse('panels:Homeworks')})
        else:
            return render(request, "Student/HomeStudent.html",{'Email':request.session['has_login']['email']})
class Homeworks(View):
    def get(self,request,*args,**kwargs):
        flag=CheckUserExistReq(request)
        if not flag:
            return HttpResponseRedirect(reverse('login:LoginPage'))
        else:
            flag=flag[0]
        if flag.userType=="Teacher":
            return render(request,"Teacher/HomeworksTeacher.html",{'Homeworks':flag.homeworks.all(),'HomeworkAddUrl':reverse('panels:HomeworkAdd')})
        else:
            return render(request,"Student/HomeworksStudent.html")
class HomeworkAdd(View):
    form_class=HomeworksAddForm
    template_name="Teacher/HomeworksAddTeacher.html"
    def get(self,request,*args,**kwargs):
        flag=CheckUserExistReq(request)
        if not flag or flag[0].userType=="Student":
            return HttpResponseRedirect(reverse('login:LoginPage'))
        flag=flag[0]
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self, request, *args, **kwargs):
        flag=CheckUserExistReq(request)
        if not flag or flag[0].userType=="Student":
            return HttpResponseRedirect(reverse('login:LoginPage'))
        flag=flag[0]
        form=self.form_class(request.POST)
        if form.is_valid():
            homework=Homework(**form.cleaned_data)
            homework.save()
            flag.addHomework(homework)
            return HttpResponseRedirect(reverse('panels:Homeworks'))
        return render(request, self.template_name, {'form': form})

        