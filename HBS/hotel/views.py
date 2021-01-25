from django.shortcuts import render, redirect
from user.models import *
from django.views.generic.list import View
# Create your views here.

class hotel_list(View):
    def get(self, request):
        hotels = Hotels.objects.all()
        return render(request, 'hotel/hotel-list.html', {'hotels':hotels})

class city(View):
    def get(self, request):
        citys = Popularlocations.objects.all()
        return render(request, 'hotel/City.html', {'citys':citys})

class home(View):
    def get(self, request):
        return render(request, 'hotel/home.html')

class Newhotel(View):
    def get(self, request):
        city = Popularlocations.objects.all()
        return render(request, 'hotel/new-hotel.html', {'city':city})

    def post(self, request):
        h_name = request.POST.get('h_name')
        address = request.POST.get('address')
        location = request.POST.get('location')
        landmark = request.POST.get('landmark')
        phone_no = request.POST.get('phone_no')

        pop_location = Popularlocations.objects.get(p_id=location)
        print(pop_location)
        Hotels.objects.create(
            location=pop_location,
            h_name=h_name,
            landmark=landmark,
            phone_no=phone_no,
            address=address
        )
        return redirect("hotel:hotel-list")

class booking(View):
    def get(self, request):
        return render(request, 'hotel/booking.html')    



class room_details(View):
    def get(self, request):
        r = Room.objects.all()
        return render(request, 'hotel/room-details.html', {'r':r})  
