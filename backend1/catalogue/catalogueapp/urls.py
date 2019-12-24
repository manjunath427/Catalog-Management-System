from django.contrib import admin
from django.urls import path,include
from .views import CategoriesListAPIView,BrandListAPIView,ProductListAPIView,CategoriesCreateAPIView,BrandCreateAPIView,ProductCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Categories/',CategoriesListAPIView.as_view(), name='Categories-list'),
    path('Brand/', BrandListAPIView.as_view(), name='Brand-list'),
    path('Product/', ProductListAPIView.as_view(), name='Product-list'),
    path('Categories/create', CategoriesCreateAPIView.as_view(), name='Categories-create'),
    path('Brand/create', BrandCreateAPIView.as_view(), name='Brand-create'),
    path('Product/create', ProductCreateAPIView.as_view(), name='Product-create'),

]
