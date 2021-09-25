from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from customer.models import Customer


def home(request):
    return render(request, 'product/home.html', {'request': request})
