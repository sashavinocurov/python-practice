from django.urls import path, include 
from .views import (
    home,
    genform,
    movielist,
    movieinfo,
)

urlpatterns = [
    path('', home),
    path('listgen/', genform),
    path('list/', movielist),
    path('info/', movieinfo),
]
