from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.

def profile(request):
    return render(request,'base.html')
    
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        roll_no = request.POST['rollnum']
        username = request.POST['uname']
        firstname = request.POST['fname'] 
        lastname = request.POST['lname']
        passwd = request.POST['pswd']
        email = request.POST['email']

        user = User.objects.create_user(username=username,password=passwd,first_name=firstname,last_name=lastname,email=email)
        user.save()
        print("User Created")
    else:
        return render(request,'register.html')

def feed(request):
    return render(request,'feed.html')

def messages(request):
    return render(request,'messages.html')

def search(request):
    return render(request,'search.html')

def tokens(request):
    return render(request,'tokens.html')