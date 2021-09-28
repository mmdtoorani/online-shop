from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from customer.models import Customer
from customer.api.serializer import *
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


def create_customer_property_func(req):
    customer = Customer.objects.create(
        username=req.POST['username'],
        email=req.POST['email'],
        phone=req.POST['phone'],
    )
    customer.save()
    customer.set_password(req.POST['password'])
    customer.save()


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        # print(request.POST)
        res = dict()
        if not len(request.POST['password']) > 8:
            if request.POST['password'] == request.POST['password2']:
                res['success'] = True
                res['link'] = '/customer/login'
                create_customer_property_func(request)
            else:
                res['success'] = False
        else:
            res['success'] = False
        return Response(res)


@api_view(['GET', 'POST'])
def customerlist(request):
    if request.method == 'GET':
        customer = get_list_or_404(Customer)
        serializer = CustomerSerializer(customer, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        customer = CustomerSerializer(data=request.data)
        if customer.is_valid():
            customer_instance = customer.save()
            customer_instance.set_password(customer.validated_data['password'])
            customer_instance.save()


@api_view(['GET', 'POST'])
def customerdetail(request, pk):
    return None


@api_view(['GET', 'POST'])
def changepassword(request):
    return None


@api_view(['GET', 'POST'])
def forgetpassword(request):
    return None
