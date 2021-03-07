from django.db import models
from panels.models import Homework
Types=[('Student','Student'),('Teacher','Teacher')]
class Person(models.Model):
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=50)
    userType=models.CharField(max_length=10)
    def exist(email,password,userType,pkUser=None):
        if userType=="Student":
            return Student.objects.filter(email=email,password=password)
        else:
            return Teacher.objects.filter(email=email,password=password)
    def __str__(self):
        return self.email
class Student(Person):
    studentCode=models.CharField(max_length=12)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.userType="Student"
class Teacher(Person):
    homeworks=[]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.userType="Teacher"
    def addHomework(self,hw):
        self.homeworks.append(hw)


