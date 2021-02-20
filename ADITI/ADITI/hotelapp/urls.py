from django.urls import path 
from . import views 

app_name='hotelapp'

urlpatterns = [
    path('hlogin', views.hlogin, name='hlogin'),
    path('hsignup', views.hsignup, name='hsignup'),
    path('r_management', views.room_management, name='r_management'),
    path('analytics', views.analytics, name='analytics'),
    path('hotel_list', views.hotel_list, name='hotel_list'),
    path('Payout', views.Payout, name='Payout'),
    path('Payment', views.Payment, name='Payment'),
    path('b_management', views.booking_management, name='b_management'),

    path('roomsadd', views.roomsadd, name='roomsadd'),

]