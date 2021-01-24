from django.urls import path
from . import views
from hotel.views import hotel_list, city, home

app_name = 'hotel'
urlpatterns = [
    path('', home.as_view(), name="home"),
    path('hotel-list', hotel_list.as_view(), name="hotel-list"),
    path('city', city.as_view(), name="city"),
]