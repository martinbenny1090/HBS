from django.shortcuts import render, redirect
from django.views.generic.list import ListView , View
from user.models import *
from django.contrib.auth.models import User, auth
# Create your views here.

class index(View):

    def get(self, request):
        return render (request, 'index.html')

    def post(self, request):
        loc = request.POST.get('loc')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        adult = request.POST.get('adult')
        children =  request.POST.get('children')
        room = request.POST.get('room')
        print(loc)
        print(check_in)
        print(check_out)
        print(adult)
        return redirect('/')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email,password=password)

        if user is not None:
            auth.login(request, user)
            if User.objects.filter(username=email, is_staff="True", is_superuser="False").exists():
                return redirect("hotel:home")
            # elif User.objects.filter(username=email, is_staff="True").exists():is_superuser="True"
            #     # messages.info(request,'Admin page')
            #     return render(request, 'hotel-list.html')
            else:
                # auth.login(request, user)
                return redirect("/")

        else:
            # messages.info(request,'Invalied Login')
            return redirect('user:login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')