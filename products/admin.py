from django.contrib import admin

# Register your models here.
from django.contrib import admin

from products.models import Products, Orders, OrdersItems

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrdersItems)