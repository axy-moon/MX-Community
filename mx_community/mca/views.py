from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import *
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def feed(request):
    User = get_user_model()
    users = User.objects.all()
    feed_dict = {'feed':Post.objects.order_by('-post_time'),'users':users}
    return render(request,'feed.html',feed_dict)

def register(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        user = NewUser.objects.create_user(rollno=rollno,username=username,email=email,password=password,first_name=firstname,last_name=lastname)
        user.save()
        return redirect('login')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rollno = request.POST['rollno']

        user = auth.authenticate(request,password=password,rollno=rollno)
        if user is not None:
            auth.login(request,user)
            return redirect('feed')
        else:
            return HttpResponse('Invalid User')
    return render(request,'login.html')


def tokens(request):
    return render(request,'tokens.html')