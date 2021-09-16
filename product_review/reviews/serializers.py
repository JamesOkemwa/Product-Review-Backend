from .models import Product, Category
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']
        # fields = '__all__'
        # exclude = ['category']
        # read_only_fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']