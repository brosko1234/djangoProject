from django.contrib.auth.views import LoginView
from django.shortcuts import render


def index(requests):
    return render (requests, 'aaa/home.html')

def register(requests):
    return render(requests, 'aaa/register.html')



