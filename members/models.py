from django.db import models

# Create your models here.
class member(models.Model):
    name = models.TextField()
    famname = models.TextField()
    cardnum=models.TextField()
    year=models.TextField()
    birth=models.DateField()
