from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Userdetails
# Create your views here.


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']  
        if CustomUser.objects.filter(username=email).exists():
            error_msg='Email id allready registered'
            return render(request, 'user/signup.html', {'error_msg':error_msg})
        elif pass1==pass2:
            user = CustomUser.objects.create_user(username=email, password=pass2, first_name=fname, last_name=lname, email=email, phone=phone)
            user.save()
            return redirect('login')
        else:
            error_msg='Passwoed not matching'
            return render(request, 'user/signup.html', {'error_msg':error_msg})
    else:
        return render(request, 'user/signup.html')


def login(request):
    error_msg = None
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None and user.is_superuser==False and user.is_hotel==False:
            auth_login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return render(request, 'user/home2.html')      
        else:
            error_msg = 'In valied login '
            return render(request, 'user/login.html', {'error_msg':error_msg})
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth_logout(request)
    return redirect('index')



def index(request):
    return render(request, 'user/index.html')

def explore(request):
    return render(request, 'user/explore.html')

def home(request):
    return render(request, 'user/home.html')

def profile(request):
    return render(request, 'user/profile.html')

@login_required(login_url='login')
def hotel_list(request):
    return render(request, 'user/home2.html')

def hotel_detail(request):
    return render(request, 'user/bookNow.html')

def user_detail(request):
    if request.method=="POST":
        name = request.POST['name']
        SurName = request.POST['SurName']
        gender = request.POST['gender']
        dob = request.POST['dob']
        email = request.POST['email']
        phone = request.POST['phone']
        image = request.FILES['image']
        user = Userdetails(name=name, surname=SurName, gender=gender, dob=dob, email=email, PhNumber=phone, Id_Proof=image)
        user.save()
        return redirect('user_detail')
    else:
        return render(request, 'user/userDetails.html')