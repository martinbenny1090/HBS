from django.shortcuts import render
from user.models import *
from django.views.generic.list import View
# Create your views here.

class hotel_list(View):
    def get(self, request):
        hotels = Hotels.objects.all()
        return render(request, 'hotel/hotel-list.html', {'hotels':hotels})