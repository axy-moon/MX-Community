from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import *
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from json import dumps
from django.db.models import Q
import random


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
        return redirect('profile_setup')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        rollno = request.POST['rollno']

        user = auth.authenticate(request,password=password,rollno=rollno)
        if user is not None:
            if user.last_login:
                auth.login(request,user)
                return redirect('feed')
            else:
                auth.login(request,user)
                return redirect('profile_setup')
        else:
            return HttpResponse('Invalid User')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def verify(request):
    global otp
    if(request.method == 'POST'):
        entered_otp = request.POST['otp']
        print(otp)
        if (int(entered_otp)==int(otp)):
            return HttpResponse('Success')
        else:
            return HttpResponse("failed")
    otp = random.randrange(1000,9999)
    print(otp)
    return render(request,"sendmail.html")


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
    event = Event.objects.all()[:2]
    print(users)  
    feed_dict = {'feed':Post.objects.order_by('-post_time'),'users':users,'events':event}
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
def profiles(request):
     
    current_user = request.user
    u = NewUser.objects.filter(rollno=current_user)
    ps = Post.objects.filter(author=current_user).order_by('-post_time')
    d = profile.objects.filter(username=current_user.id)
    print(d)
    cont = {'profile':d,'ps':ps}
    return render(request,'profile.html',cont)

@login_required
def prosetup(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        add1 = request.POST['Add1']
        add2 = request.POST['Add2']
        pin = request.POST['pin']
        sA = request.POST['student']
        work = request.POST['work']
        role = request.POST['role']
        s1 = request.POST['skill1']
        s2 = request.POST['skill2']
        dob = request.POST['dob']
        gender = request.POST['gender']

        current_user = request.user
        username = NewUser.objects.get(username=current_user.username)
        status = True
        if sA == 'alumni':
            status = False


        profile.objects.create(username=username,workplace=work,phone=phone,address_line_1=add1,address_line_2=add2,pin=pin,gender=gender,dob=dob,skill1=s1,skill2=s2,is_student=status)
        print("Stored")
        return redirect('feed')
    return render(request,'data.html')


def search(request):
    if request.method == 'GET':
        a =  request.GET.get('q')
        
        if a is not None:
            lookups = Q(title__icontains=a) | Q(content__icontains=a)
            results = Post.objects.filter(lookups).distinct()
            print(results)
            context = {'results': results,'a':a}
            return render(request,'search.html',context)
        return render(request,'search.html')
    else:
        return render(request,'search.html')

    