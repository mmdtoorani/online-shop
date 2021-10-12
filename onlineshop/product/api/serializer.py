from rest_framework import serializers
from product.models import Product, Category


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(
        source='category.category_name',
        read_only=True,
    )

    class Meta:
        model = Product
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
