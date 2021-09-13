from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'stock', 'availability', ]
    # list_filter = ['customer']
    list_editable = ['stock', 'availability', ]
