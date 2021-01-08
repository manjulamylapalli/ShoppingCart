from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from products.models import Products, OrdersItems, Orders


class product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'image', 'price', 'created_at', 'updated_at')


class orders_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'userid', 'total', 'created_at', 'updated_at', 'status', 'mode_of_payment')


class orders_items_Serializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersItems
        fields = ('id', 'order_id', 'product_id', 'quantity', 'price')


# Token based
from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
class user_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    Password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Confirm_Password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'Password', 'Confirm_Password', 'email')

    def validate(self, attrs):
        if attrs['Password'] != attrs['Confirm_Password']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],

        )

        user.set_password(validated_data['Password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    Confirm_Password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'Password', 'Confirm_Password')

    def validate(self, attrs):
        if attrs['Password'] != attrs['Confirm_Password']:
            raise serializers.ValidationError({"Password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"Previous_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['Password'])
        instance.save()

        return instance
