from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')