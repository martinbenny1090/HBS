from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def login(request):
    error_msg = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None and user.is_hotel==False:
            login(request, user)
            return redirect('h_search')
        else:
            error_msg = 'In valied login '
            return redirect(request, 'user/login.html', {'error_msg':error_msg})
    else:
        return render(request, 'user/login.html')


def logout(request):
    logout(request)
    return redirect('login')


def register(request):
    return render(request, 'user/signup.html')


def index(request):
    return render(request, 'user/index.html')

def explore(request):
    return render(request, 'user/explore.html')

def home(request):
    return render(request, 'user/home.html')