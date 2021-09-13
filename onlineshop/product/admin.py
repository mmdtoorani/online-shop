from django.contrib import admin
from product.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'stock', 'price', ]
    list_editable = ['stock', ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
