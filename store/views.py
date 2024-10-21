from django.shortcuts import render
from .models import Brand


def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands.html', {'brands': brands})


def categories(request):
    return render(request, 'categories.html')


def products(request):
    return render(request, 'products.html')
