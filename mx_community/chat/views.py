from django.shortcuts import render
from mca.models import *
from chat.models import *

# Create your views here.

def chat(request):
    #.by_user(user=request.user).prefetch_related('chatmessage_thread').
    threads = Thread.objects.order_by('timestamp')
    context = {
        'Threads' : threads
    }

    print(context)


    return render(request,'chat.html',context)