from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    percent = models.PositiveIntegerField()
    initial_price = models.PositiveIntegerField(null=True, blank=True)
    final_price = models.PositiveIntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='./product/media', null=True, blank=True)
    stock = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name}'

    @property
    def generate_final_price(self):
        self.final_price = self.initial_price - (self.initial_price * self.percent)
        return self.final_price
