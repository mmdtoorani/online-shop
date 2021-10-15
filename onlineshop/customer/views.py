from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response

from customer.forms import EditProfileForm
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
        return render(request, 'customer/profile.html', {
            'request': request,
            'phone': phone,
            'address': address,
        })
    if request.method == 'POST':
        pass


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer:profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'customer/profile_edit.html', context)


def cart(request):
    if request.method == 'POST':
        res = {'success': 'true'}
        print(request.POST)
        return Response(res)

    return render(request, 'customer/cart.html', {'request': request})


def auth_logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})
