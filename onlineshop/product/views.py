from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from customer.models import Customer


def home(request):
    if request.method == 'GET':
        return render(request, 'product/home.html', {'request': request})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if str(Customer.objects.all().get(username=username)) == username:
            if Customer.objects.get(username=username).password == password:
                print('rad shod')
                return render(request, 'product/home.html', {'request': request})
            else:
                return HttpResponse('<h1>password ehtebah</h1>')
        else:
            return HttpResponse('<h1>username eshtebah</h1>')

