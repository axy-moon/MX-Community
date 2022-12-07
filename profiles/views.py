from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'base.html')
    
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = requset.POST[]
        
    return render(request,'register.html')

def feed(request):
    return render(request,'feed.html')

def messages(request):
    return render(request,'messages.html')

def search(request):
    return render(request,'search.html')

def tokens(request):
    return render(request,'tokens.html')