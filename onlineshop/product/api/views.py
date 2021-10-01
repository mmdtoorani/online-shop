from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from product.api.serializer import ProductsListSerializer, CategoryListSerializer
from product.models import Product, Category


class ProductViewSet(viewsets.ViewSet):
    def productlist(self, request):
        queryset = get_list_or_404(Product)
        serializer = ProductsListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def category(self, request, pk):
        queryset = get_list_or_404(Category, id=pk)
        serializer = ProductsListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    def category_list(self, request):
        queryset = get_list_or_404(Category)
        serializer = CategoryListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
