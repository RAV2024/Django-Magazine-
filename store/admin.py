from django.contrib import admin
from .models import Brand, Category, Product, ProductImage

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
