from django.db import models
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # AVAILABLE = 'AVAILABLE'
    # UNAVAILABLE = 'UNAVAILABLE'
    # availability_choices = (
    #     (AVAILABLE, 'AVAILABLE'),
    #     (UNAVAILABLE, 'UNAVAILABLE')
    # )
    # availability = models.CharField(choices=availability_choices, max_length=100, default=AVAILABLE)
    count = models.PositiveIntegerField()
