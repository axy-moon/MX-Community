from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.utils import timezone
# Create your models here.

class NewUser(AbstractUser):
    rollno = models.CharField(max_length=7,null=False,unique=True,verbose_name='Roll Number')
    USERNAME_FIELD = 'rollno'

class Post(models.Model):
    author = models.ForeignKey(NewUser,on_delete=CASCADE)
    title = models.CharField(max_length=30,default='Question')
    category = models.CharField(max_length=40,default='Others')
    post_time = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to='posts',blank=True)
    content = models.TextField(null=False)
    comment = models.TextField(blank=True,)

    def __str__(self):
        return self.title

class tokens(models.Model):
    roll_no = models.CharField(max_length=7,null=False,unique=True,verbose_name='Roll No')
    first_name = models.CharField(max_length=50,verbose_name='First Name')
    last_name = models.CharField(max_length=50,verbose_name='Last Name')

    def __str__(self):
        return self.roll_no

class profile(models.Model):
    username = models.ForeignKey(NewUser,on_delete=CASCADE)
    workplace = models.CharField(max_length=30,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True)
    gender = models.CharField(max_length=10,null=False,default='Male')
    dob = models.DateField(blank=True,default='2001-08-08')
    address_line_1 = models.CharField(max_length=50,null=True)
    address_line_2 = models.CharField(max_length=50,null=True)
    pin = models.IntegerField()
    skill1 = models.CharField(max_length=50,blank=True)
    skill2 = models.CharField(max_length=50,blank=True)
    is_student = models.BooleanField(default=True)

    
    def __str__(self):
        return self.username.rollno


class Event(models.Model):
    event_name = models.CharField(max_length=100,verbose_name="Event name")
    event_date = models.DateField(verbose_name='Date')
    event_location = models.CharField(max_length=100,verbose_name='Location')