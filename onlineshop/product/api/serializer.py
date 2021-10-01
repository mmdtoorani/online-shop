from rest_framework import serializers
from product.models import Product, Category


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='category',
        lookup_field='pk'
    )

    class Meta:
        model = Product
        # fields = ['percent', 'product_name', 'category', 'initial_price',
        #           'final_price', 'description', 'stock']
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
