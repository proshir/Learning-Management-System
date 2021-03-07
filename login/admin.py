from django.contrib import admin
from .models import Student,Teacher,Person
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields=('email','password')
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields=('email','password')

