from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic.list import ListView , View
# Create your views here.

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


class c_register(View):
    def get(self, request):
        return render(request, "u-registration.html")


def hotel_login(request):
    return render(request, 'hotel/login.html')

class hotel_registration(View):
    def get(self, request):
        return render(request, 'hotel/hotel-registration.html')