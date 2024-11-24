from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Category, Product
from .forms import BrandForm, UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')


def brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brands.html', {'brands': brands})

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})




def categories(request):
    categories = Category.objects.filter(parent=None)
    return render(request, 'categories/categories.html', {'categories': categories})



def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(Category, id=subcategory_id)
    products = Product.objects.filter(category=subcategory)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    if sort == 'asc':
        products = products.order_by('price')
    elif sort == 'desc':
        products = products.order_by('-price')
    return render(request, 'categories/products_by_subcategory.html',
                  {'subcategory': subcategory,
                   'products': products,
                   'sort': sort,
                   })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'categories/product_detail.html', {'product': product})


def products(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})

def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brands')
    else:
        form = BrandForm()
    return render(request, 'brands/create_brand.html', {'form': form})



def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, 'Бренд был успешно удален.')
        return redirect('brands')

    return render(request, 'brands/delete_brand.html', {'brand': brand})


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

    return render(request, 'brands/edit_brand.html', {'form': form, 'brand': brand})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = []

    if product.category.requires_size:
        sizes = ["35.5", "36", "36.5", "37", "37.5", "38", "38.5", "39", "40", "40.5",
                 "41", "41.5", "42", "42.5", "43", "43.5", "44", "44.5", "45", "45.5",
                 "46", "46.5", "47", "47.5", "48", "48.5"]

    return render(request, 'categories/product_detail.html', {'product': product, 'sizes': sizes})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему.')
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин или пароль.')
    else:
        form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})