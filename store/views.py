from django.shortcuts import render
from .models import Brand
from .models import Category
from .models import Product


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands.html', {'brands': brands})


def categories(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'categories.html', {'categories': categories})


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


