from django.db import models
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    availability_choices = (
        (AVAILABLE, 'AVAILABLE'),
        (UNAVAILABLE, 'UNAVAILABLE')
    )
    availability = models.CharField(choices=availability_choices, max_length=100, default=AVAILABLE)

    def __str__(self):
        return f'{self.customer.first_name} {self.customer.last_name} | {self.product.name}'
