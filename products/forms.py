import django.forms as forms
from .models import Products, Orders, OrdersItems


class Products_Form(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class orders_Form(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


class orders_items_Form(forms.ModelForm):
    class Meta:
        model = OrdersItems
        fields = '__all__'
