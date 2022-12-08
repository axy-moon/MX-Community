from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class NewUser(AbstractUser):
    rollno = models.CharField(max_length=7,null=False)
    