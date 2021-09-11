from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    count = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
