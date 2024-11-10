from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand
from .models import Category
from .models import Product
from .forms import BrandForm
from django.contrib import messages




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

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    return render(request, 'products_by_subcategory.html', {'subcategory': subcategory, 'products': products})



def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})



def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brands')
    else:
        form = BrandForm()
    return render(request, 'create_brand.html', {'form': form})



def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Бренд был успешно удален.')
        return redirect('brands')

    return render(request, 'delete_brand.html', {'brand': brand})


def edit_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бренд успешно обновлен.')
            return redirect('brands')
    else:
        form = BrandForm(instance=brand)

    return render(request, 'edit_brand.html', {'form': form, 'brand': brand})







