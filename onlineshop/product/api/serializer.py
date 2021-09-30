from rest_framework import serializers
from product.models import Product


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category',
    )

    class Meta:
        model = Product
        # fields = ['percent', 'product_name', 'category', 'initial_price',
        #           'final_price', 'description', 'stock']
        fields = '__all__'
