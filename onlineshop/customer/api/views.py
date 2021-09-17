from rest_framework.response import Response
from rest_framework.decorators import api_view
from customer.models import Customer
from customer.api.serializer import *
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        pass


@api_view(['GET', 'POST'])
def customerlist(request):
    if request.method == 'GET':
        customer = get_list_or_404(Customer)
        serializer = CustomerSerializer(customer, context={'request': request})
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def customerdetail(request, pk):
    return None



