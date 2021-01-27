from django.urls import path
from . import views
from user.views import index

app_name = "user"

urlpatterns = [
    path("", index.as_view(), name='index'),
    
]