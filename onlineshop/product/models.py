from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=80)
    percent = models.PositiveIntegerField(default=0, blank=True)
    initial_price = models.PositiveIntegerField(default=0, blank=True)
    final_price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    photo = models.ImageField(upload_to='./product/media', null=True, blank=True)
    stock = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.product_name

    @property
    def generate_final_price(self):
        self.final_price = self.initial_price - (self.initial_price * self.percent)
        return self.final_price
