from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout 
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    error_msg = None
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = authenticate(username=email,password=password)
        if user is not None and user.is_employee==False:
            auth_login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return render(request, 'hotel/index.html')      
        else:
            error_msg = 'In valied login '
            return render(request, 'user/login.html', {'error_msg':error_msg})
    else:
        return render(request, 'user/login.html')

# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         user = auth.authenticate(username=email,password=password)

#         if user is not None:
#             auth.login(request, user)
#             if CustomUser.objects.filter(username=email, is_superuser="True").exists():
#                 # messages.info(request,'Admin page')
#                 return render(request, 'hotel/index.html')
#             else:
#                 # auth.login(request, user)
#                 return redirect("/")

#         else:
#             # messages.info(request,'Invalied Login')
#             return redirect('login')

#     else:
#         return render(request, 'user/login.html')

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

def hotelHome(request):
    return render(request, 'hotel/index.html')