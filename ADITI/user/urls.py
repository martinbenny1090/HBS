from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_done.html"), name="password_reset_complete"),

    path('home/', views.home, name='home'),#user search page
    path('explore/', views.explore, name='explore'),
    path('hotel/', views.hotelHome, name='hotel/'),



    
]