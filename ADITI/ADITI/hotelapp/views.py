from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import CustomUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Hotel, Room
# Create your views here.

def hsignup(request):
    error_msg=None
    if request.method == 'POST':
        hname = request.POST['hname']
        city = request.POST['city']
        email = request.POST['email']
        landmark = request.POST['landmark']
        zip_code = request.POST['zip_code']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if CustomUser.objects.filter(username=email).exists():
            error_msg='Email id allready registered'
            return render(request, 'hotel/hsignup.html', {'error_msg':error_msg})
        elif pass1==pass2:
            h =CustomUser.objects.create_user(username=email, password=pass2, email=email, phone=phone, is_hotel=True, is_staff=True)
            h.save()
            hotel = Hotel(Hname=hname, city=city, landmark=landmark, email=email, zip_code=zip_code, phone=phone)
            hotel.save()
            return redirect('hotelapp:hlogin')
        else:
            error_msg='Passwoed not matching'
            return render(request, 'hotel/hsignup.html', {'error_msg':error_msg})
    else:
        return render(request, 'hotel/hsignup.html')


def hlogin(request):
    error_msg = None
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None and user.is_hotel==True:
            auth_login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('hotelapp:b_management')      
        else:
            error_msg = 'In valied login '
            return render(request, 'user/login.html', {'error_msg':error_msg})
    else:
        return render(request, 'hotel/hlogin.html')


def roomsadd(request):
    '''model page to the room adding to the database'''
    error_msg=None
    if request.method == 'POST':
        r_no = request.POST['r_no']
        price = request.POST['price']
        discount = request.POST['discount']
        tax = request.POST['tax']
        R_type = request.POST['r_type']
        image = request.FILES['image']
        image1 = request.FILES['img1']
        image2 = request.FILES['img2']
        image3 = request.FILES['img3']
        
        room = Room(HotelName=request.user, Rno=r_no, price=price, discount=discount, tax=tax, image=image, img1=image1, img2=image2, img3=image3)
        room.save()
        return redirect('hotelapp:r_management')
    else:    
        return render(request, 'hotel/r_mngModel.html')

@login_required(login_url='hotelapp:hlogin')
def room_management(request):
    return render(request, 'hotel/r_mngmnt.html')
    


def analytics(request):
    return render(request, 'hotel/analytics.html')


def hotel_list(request):
    return render(request, 'hotel/h_list.html')


def Payout(request):
    return render(request, 'hotel/p_out.html')


def Payment(request):
    return render(request, 'hotel/pymnt.html')


def booking_management(request):
    return render(request, 'hotel/b_mngmnt.html')