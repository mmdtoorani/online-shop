from django.contrib.auth import logout
from django.shortcuts import render


def login(request):
    return render(request, 'customer/login.html', {'request': request})


def signup(request):
    return render(request, 'customer/signup.html', {'request': request})


def profile(request):
    return render(request, 'customer/profile.html', {'request': request})


def orderhistory(request):
    return render(request, 'customer/orderhistory.html', {'request': request})


def auth_logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})
