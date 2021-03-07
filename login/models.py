from django.db import models

class Person(models.Model):
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=50)