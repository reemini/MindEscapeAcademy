from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'page/signup.html')

def login(request):
    return render(request, 'page/login.html')

def courseinfo(request):
    return render(request,'page/courseinfo.html')

def header(request):
    return render(request,'part/header.html')

def forgetpass(request):
    return render(request, 'page/forgetpass.html')