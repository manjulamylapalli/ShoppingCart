from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.image} - {self.price} - {self.created_at}- {self.updated_at} "


class Orders(models.Model):
    payment_choices = (
        ('cash', 'Cash'),
        ('paytm', 'Paytm'),
        ('card', 'Card'),
    )

    status_choices = (
        ('new', 'New'),
        ('paid', 'Paid')

    )
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_choices)
    mode_of_payment = models.CharField(max_length=30, choices=payment_choices)

    def __str__(self):
        return f"{self.userid} - {self.total} - {self.created_at} - {self.updated_at} - {self.status} - {self.mode_of_payment} "


class OrdersItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.order_id} - {self.product_id} - {self.quantity} - {self.price} "



