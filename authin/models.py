from django.db import models

# Create your models here.
class user_a(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,unique=True)#unique
    pass_word=models.CharField(max_length=30)

