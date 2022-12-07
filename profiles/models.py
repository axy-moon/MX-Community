from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    rollno = models.CharField(max_length=7,null=False)

class profile