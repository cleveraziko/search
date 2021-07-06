from django.shortcuts import render
from django.urls import  path

# Create your views here.



def home(request):
    return render(request,'base.html')


def new_search(request):
    return render(request, 'new_search.html')