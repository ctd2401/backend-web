from rest_framework import serializers
from django.db import models
from products.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'summary' ]