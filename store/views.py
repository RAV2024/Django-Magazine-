from django.shortcuts import render, get_object_or_404
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

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brand_detail.html', {'brand': brand})


def categories(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'categories.html', {'categories': categories})

def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Category, id=subcategory_id)
    products = Product.objects.filter(category=subcategory)
    return render(request, 'products_by_subcategory.html', {'subcategory': subcategory, 'products': products})


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


