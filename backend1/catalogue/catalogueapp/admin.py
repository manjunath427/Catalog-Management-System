from django.contrib import admin
from .models import Categories,Brand,Product

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','parent_category','data_created','last_modifiction']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','data_created','last_modifiction']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','brand','category','data_created','last_modifiction','specification']



admin.site.register(Categories,CategoriesAdmin)
admin.site.register( Brand,BrandAdmin)
admin.site.register( Product,ProductAdmin)



