from django.shortcuts import render

from products.models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategoryListSerializer, ProductListSerializer
# Create your views here.


class CategoryListView(APIView):

    def get(self, request, category_slug=None):
        categories = Category.objects.all()
        products = Product.objects.filter(status=True)
        category_serializer = CategoryListSerializer(categories, many=True)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category)
        product_serializer = ProductListSerializer(products, many=True)
        print(product_serializer)
        print()
        print(product_serializer.data)
        response_data = {
            'products': product_serializer.data,
            'categories': category_serializer.data
        }
        return Response
