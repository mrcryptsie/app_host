from django.contrib import admin
from .models import Carts, CartsItem

# Register your models here.

admin.site.register(Carts)
admin.site.register( CartsItem)