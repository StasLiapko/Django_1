from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app_1(request):
    return HttpResponse('<h1>Hello from app_1</h1>')

def index(request):
     return HttpResponse('<h1>Index</h1>')
