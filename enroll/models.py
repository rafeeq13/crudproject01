from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    #Ph_No=models.IntegerField()
    father_Name=models.CharField(max_length=70)
    Address=models.CharField(max_length=150)
    #Resume=models.FileField()
