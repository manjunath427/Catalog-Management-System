from  rest_framework import serializers
from  .models import Categories,Brand,Product




class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CreateCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'




class CreateBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


