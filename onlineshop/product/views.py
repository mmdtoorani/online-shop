from django.contrib.auth import authenticate, login
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
        user = authenticate(username=username, password=password)
        # print(request.POST['password2'])
        print('user authenticate shod!!!')
        if user:
            print('user is not None!!!')
            login(request, user)
            print('user has been login')
            return render(request, 'product/home.html', {'request': request})

        # if Customer.objects.get(username=username).username == username:
        #     if Customer.objects.get(username=username).password == password:
        #         print('rad shod')
        #         login()
        #         return render(request, 'product/home.html', {'request': request})
        #     else:
        #         return HttpResponse('<h1>password ehtebah</h1>')
        # else:
        #     return HttpResponse('<h1>username eshtebah</h1>')

