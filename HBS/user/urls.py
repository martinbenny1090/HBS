from django.urls import path
from . import views
from user.views import  search, index

urlpatterns = [
    path("", index.as_view(), name='index'),
    path("search/", search.as_view(), name="search"),
]