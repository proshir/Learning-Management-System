from django.db import models
from panels.models import Homework
from django.utils.timezone import now
Types=[('Student','Student'),('Teacher','Teacher')]
class Person(models.Model):
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=50)
    userType=models.CharField(max_length=10)
    def exist(email,password,userType,pkUser=None):
        if userType=="Student":
            return Student.objects.filter(email=email,password=password)
        else:
            return Teacher.objects.filter(email=email,password=password)
    def __str__(self):
        return self.email
class SentHomework(models.Model):
    homework=models.OneToOneField(Homework,on_delete=models.CASCADE,related_name="SentHomework",primary_key=True)
    #LastSumbit=models.DateTimeField(null=True, blank=True,verbose_name=u'LastSumbit',default=None)
    Answer=models.FileField(upload_to='uploads/')
    Result=models.FloatField(null=True)
class Student(Person):
    studentCode=models.CharField(max_length=12)
    homeworks=models.ManyToManyField(SentHomework,related_name="Student")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.userType="Student"
        self.save()
        for hw in Homework.objects.all():
            if self.homeworks.filter(homework=hw):
                continue
            sentHomework=SentHomework(homework=hw)
            sentHomework.save()
            self.homeworks.add(sentHomework)
        self.save()
class Teacher(Person):
    homeworks=models.ManyToManyField(Homework,related_name='Teacher')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.userType="Teacher"
        self.save()
    def addHomework(self,hw):
        self.save()
        self.homeworks.add(hw)
        print("hello")
        for student in Student.objects.all():
            if student.homeworks.filter(homework=hw):
                print(student.homeworks.filter(homework=hw))
                continue
            sentHomework=SentHomework(homework=hw)
            student.homeworks.add(sentHomework)
            student.save()
        self.save()



