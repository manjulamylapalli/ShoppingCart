# from rest_framework.authentication import BasicAuthentication
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from products.models import Products, OrdersItems, Orders
from products.serializers import product_Serializer, orders_Serializer, orders_items_Serializer


class productList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = product_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class productDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = product_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class orderList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = orders_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class orderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = orders_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]


class orders_items_List(generics.ListCreateAPIView):
    queryset = OrdersItems.objects.all()
    serializer_class = orders_items_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class orders_items_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdersItems.objects.all()
    serializer_class = orders_items_Serializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

