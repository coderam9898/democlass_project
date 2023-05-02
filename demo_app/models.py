from django.db import models
import datetime

# Create your models here.

class demousers(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class todo(models.Model):
    task = models.CharField(max_length=255 )
    task_created = datetime.datetime.now() 

class simpletodo(models.Model):
    task = models.CharField(max_length=255, unique=True )
    task_created = datetime.datetime.now() 