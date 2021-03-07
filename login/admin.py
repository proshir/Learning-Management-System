from django.contrib import admin
from .models import Student,Teacher
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields=('email','password','studentCode')
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields=('email','password')

