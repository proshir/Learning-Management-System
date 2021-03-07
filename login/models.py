from django.db import models
Types=[('Student','Student'),('Teacher','Teacher')]
class Person(models.Model):
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=50)
    userType=models.CharField(max_length=10)
    def exist(email,password,userType):
        if userType=="Student":
            return Student.objects.filter(email=email,password=password)
        else:
            return Teacher.objects.filter(email=email,password=password)
class Student(Person):
    pass
class Teacher(Person):
    pass
    