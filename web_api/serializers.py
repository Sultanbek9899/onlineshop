from rest_framework import serializers
from store.products.models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category',
                  'name',
                  'slug',
                  'image',
                  'description',
                  'price',
                  'created',]