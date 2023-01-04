from django.db import models
from mca.models import *
from django.db.models import Q
# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self,**kwargs):
        user = kwargs.get('user')
        lookup = Q(first_user=user) | Q(second_user=user)
        qs = self.get_queryset().filter(lookup).distinct()

class Thread(models.Model):
    first_user = models.ForeignKey(NewUser,on_delete=CASCADE,null=True,related_name='thread_first_user')
    second_user = models.ForeignKey(NewUser,on_delete=CASCADE,null=True,related_name='thread_second_user')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()

    class Meta:
        unique_together = ['first_user','second_user']

class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread,null=True,blank=True,on_delete=CASCADE,related_name='chatmessage_thread')
    user = models.ForeignKey(NewUser,on_delete=CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



