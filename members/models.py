from django.db import models

# Create your models here.
class member(models.Model):
    name = models.CharField(max_length=30)
    famname = models.CharField(max_length=30)#unique
    cardnum=models.CharField(max_length=10,unique=True)
    year=models.CharField(max_length=30)
    birth=models.DateField()
