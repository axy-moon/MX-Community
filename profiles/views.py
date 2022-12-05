from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'base.html')
    
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def feed(request):
    return render(request,'feed.html')