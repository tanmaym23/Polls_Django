from django.db import models

# Create your models here.

class student(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=250)
    course=models.CharField(max_length=250)

class course(models.Model):
    pass