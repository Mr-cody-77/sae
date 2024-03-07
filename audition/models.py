from django.db import models

# Create your models here.

class mydata(models.Model):
    name=models.CharField(max_length=80)
    roll=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
    phone=models.IntegerField(max_length=20)