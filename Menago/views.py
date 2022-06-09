from django.shortcuts import render
from .forms import TaskiWyswietlanie
from .models import Taski
from django.urls import is_valid_path
from django.http import HttpResponse


# Create your views here.
def home_page(request, *args, **kwargs):
    #dodawanie zadania
    zapytanie=TaskiWyswietlanie(request.POST)
    if zapytanie.is_valid():
        zapytanie.save()
        zapytanie=TaskiWyswietlanie()
    else:
        print(zapytanie.errors)
    
    #wyswietlanie danych

    objekt=Taski.objects.all()

    zwracacz={
        'dodanie':zapytanie,
        'obj':objekt,

    }
    return render(request,'index.html',zwracacz)