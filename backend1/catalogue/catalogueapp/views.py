from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Categories,Brand,Product
from .serializers import *

# Create your views here.

class CategoriesListAPIView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesCreateAPIView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer



class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer









