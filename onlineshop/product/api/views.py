from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from product.api.serializer import ProductsListSerializer, CategoryListSerializer
from product.models import Product, Category


class ProductAPIView(APIView):
    serializer = ProductsListSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            category = request.query_params["category"]
            if category:
                product = Product.objects.filter(category__category_name=category)
                serializer = ProductsListSerializer(product, many=True)
                return Response(serializer.data)
        except:
            product = self.get_queryset()
            serializer = ProductsListSerializer(product, many=True)

        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    def category_list(self, request):
        queryset = get_list_or_404(Category)
        serializer = CategoryListSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)
