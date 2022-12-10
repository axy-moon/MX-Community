from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_DEFAULT


# Create your models here.

class NewUser(AbstractUser):
    rollno = models.CharField(max_length=7,null=False,unique=True,verbose_name='Roll Number')
    USERNAME_FIELD = 'rollno'

class Post(models.Model):
    author = models.ForeignKey(NewUser,on_delete=CASCADE)
    title = models.CharField(max_length=30,default='Post')
    post_time = models.DateTimeField()
    content = models.TextField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title

