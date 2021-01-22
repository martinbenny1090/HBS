from django.urls import path
from . import views
from hotel.views import hotel_list
urlpatterns = [
    path('hotel-list', hotel_list.as_view(), name="hotel-list"),
]