from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'horror/home.html')

def genform(request):
    return render(request, 'horror/genform.html')

def movielist(request):
    return render(request, 'horror/movielist.html')

def movieinfo(request):
    return render(request, 'horror/movieinfo.html')