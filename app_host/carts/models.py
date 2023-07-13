from django.db import models
from store.models import Product

# Create your models here.

class Carts(models.Model):
    carts_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carts_id

class CartsItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    carts    = models.ForeignKey(Carts, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.product