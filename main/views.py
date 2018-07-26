from django.shortcuts import render
import requests

def home(request):
    return render (request, 'main/home.html')

# Create your views here.
