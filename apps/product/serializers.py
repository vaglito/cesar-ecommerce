from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price', 'slug', 'created_at']