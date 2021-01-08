"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from products import serializers
from products.account_views import RegisterView,ChangePasswordView,loginAPI
from products import restviews, account_views

urlpatterns = [
    path('admin/', admin.site.urls),


    # path('account/<str:user>/',UserViewSet),
    path("products_items/", restviews.productList.as_view()),
    path("products_details/<int:pk>", restviews.productDetails.as_view()),

    path("order_list/", restviews.orderList.as_view()),
    path("order_details/<int:pk>", restviews.orderDetails.as_view()),
    # order
    path("orderitems_list/", restviews.orders_items_List.as_view()),
    path("order_details/<int:pk>", restviews.orderDetails.as_view()),

#    Authentication
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/change_password/', ChangePasswordView.as_view(), name='register'),
    path('api/login/', loginAPI.as_view(), name='login'),
    # path('api/logout/', account_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', account_views.LogoutAllView.as_view(), name='logoutall')
]
