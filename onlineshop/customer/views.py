from django.shortcuts import render
from customer.forms import *


def signup(request):
    context = dict()
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            if Customer.objects.filter(id=customer.id):
                form = SignupForm()

            else:
                customer.save()

                return render(request, 'customer/login.html', context)
    context['form'] = form
    return render(request, 'customer/signup.html', context)


def login(request):
    pass
