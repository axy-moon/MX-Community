from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.db.models.fields import AutoField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class NewUser(AbstractUser):
    rollno = models.CharField(null=False,max_length=7)
    year = models.DateField()

""" 
class profile(models.Model):
    firstname = models.ForeignKey(User,on_delete=CASCADE)
    lastname = models.ForeignKey(User,on_delete=CASCADE)
    pro_pic = models.ImageField()
    group = models.ForeignKey(User,on_delete=CASCADE)
    year = models.DateField()
    bio = models.TextField()

class Posts(models.Model):
    title = models.CharField(max_length=100,null=False)
    content = models.TextField()
    time_posted = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=CASCADE)
    image = models.ImageField()
    comments = models.TextField()


class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=CASCADE)
    reciever = models.ForeignKey(User,on_delete=CASCADE)
    timestamp = models.DateTimeField()
    message = models.TextField()

class Tokens(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=7)
    year = models.DateField() """