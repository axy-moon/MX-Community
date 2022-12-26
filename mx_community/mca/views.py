from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import *
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from json import dumps

# Create your views here.
def home(request):
    return render(request,'home.html')


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
        password = request.POST['password']
        rollno = request.POST['rollno']

        user = auth.authenticate(request,password=password,rollno=rollno)
        if user is not None:
            auth.login(request,user)
            return redirect('feed')
        else:
            return HttpResponse('Invalid User')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def feed(request):
    User = get_user_model()
    if request.method == 'POST':
        content = request.POST['postcontent']
        title = request.POST['postTitle']
        current_user = request.user
        author = NewUser.objects.get(rollno=current_user.rollno)

        Post.objects.create(author=author,content=content,title=title)
        return redirect('feed')
   
    users = User.objects.all()
    print(users)  
    feed_dict = {'feed':Post.objects.order_by('-post_time'),'users':users}
    return render(request,'feed.html',feed_dict)

@login_required
def token(request):
    current_user = request.user
    roll_t = current_user.rollno[-1]
    print(roll_t)
    names = tokens.objects.filter(roll_no__endswith=roll_t)
    print(names)
    d = {'token':names}
    return render(request,'tokens.html',d)

@login_required
def messages(request):
    return render(request,'messages.html')

@login_required
def profile(request):
    return render(request,'profile.html')