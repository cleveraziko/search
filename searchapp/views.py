import requests
from django.shortcuts import render
from django.urls import  path
from bs4 import BeautifulSoup

# Create your views here.



def home(request):
    return render(request,'base.html')


def new_search(request):
    search = request.POST.get('search', )
    stuff_for_frontend = {
        'search': search
    }
    return render(request, 'new_search.html', stuff_for_frontend)