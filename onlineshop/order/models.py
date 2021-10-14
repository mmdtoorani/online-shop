from django.db import models
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)

    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    availability_choices = (
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    )
    availability = models.CharField(choices=availability_choices, max_length=100, default=AVAILABLE)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL)
    stock = models.PositiveIntegerField(default=0)
