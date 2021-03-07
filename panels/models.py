from django.db import models
from django.utils.timezone import now
class Homework(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200,blank=True)
    deadline=models.DateTimeField( default=now)
    def __str__(self):
        return self.name
