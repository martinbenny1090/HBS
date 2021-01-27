from django.urls import path
from . import views
from accounts.views import c_register, hotel_registration

app_name = 'accounts'

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('c_register', c_register.as_view(), name="c_register"),
    path('hotel_login', views.hotel_login, name="hotel_login"),
    path('h_register', hotel_registration.as_view(), name="h_register"),
]
    