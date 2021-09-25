from django.shortcuts import render


def login(request):
    print("request ta inja reside")
    return render(request, 'customer/login.html', {'request': request})


def signup(request):
    return render(request, 'customer/signup.html', {'request': request})


def logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})
