from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from product.api.serializer import ProductsListSerializer, CategoryListSerializer
from product.models import Product, Category


class ProductAPIView(APIView):
    serializer = ProductsListSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get(self, request, category=None):
        if category:
            queryset = get_list_or_404(Product, category__category_name=category)
        else:
            queryset = Product.objects.all()

        serializer = ProductsListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class CategoryAPIView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategoryListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

#
# class ProductByPkAPIView(APIView):
#     serializer = ProductsListSerializer
#
#     def get(self, request, pk=None):
#         if pk:
#             queryset = get_object_or_404(Product, id=pk)
#         else:
#             queryset = Product.objects.all()
#
#         serializer = ProductsListSerializer(queryset, context={'request': request})
#         return Response(serializer.data)
