from django.contrib.auth import logout
from django.shortcuts import render

from customer.models import Customer


def login(request):
    return render(request, 'customer/login.html', {'request': request})


def signup(request):
    return render(request, 'customer/signup.html', {'request': request})


def forgetpassword(request):
    return render(request, 'customer/forget_password.html', {'request': request})


def profile(request):
    if request.method == 'GET':
        this_user = Customer.objects.get(id=request.user.id)
        phone = this_user.phone
        address = this_user.address
        print(phone, address)
        return render(request, 'customer/profile.html', {
            'request': request,
            'phone': phone,
            'address': address,
        })
    if request.method == 'POST':
        pass


def profile_edit(request):
    return render(request, 'customer/profile_edit.html', {'request': request})


def orderhistory(request):
    return render(request, 'customer/orderhistory.html', {'request': request})


def cart(request):
    return render(request, 'customer/cart.html', {'request': request})


def auth_logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})
