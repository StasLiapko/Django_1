from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app_2(request):
    return HttpResponse('<h1>Hello from app_2</h1>')