from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/signup.html')
