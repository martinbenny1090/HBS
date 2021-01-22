from django.shortcuts import render, redirect
from django.views.generic.list import ListView , View
from user.models import *

# Create your views here.
class index(View):
    def get(self,request):
        return render(request, 'index.html')

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


class search(View):
    def get(self, request):
        hotels = Hotels.objects.all()
        return render(request, 'hotels_list.html', {'hotels':hotels})
