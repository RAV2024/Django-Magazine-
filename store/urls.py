from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import register, user_login
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', views.home, name='home'),

    path('brands/', views.brands, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('brands/new/', views.create_brand, name='create_brand'),
    path('brands/<int:brand_id>/delete/', views.delete_brand, name='delete_brand'),
    path('brands/<int:brand_id>/edit/', views.edit_brand, name='edit_brand'),

    path('categories/', views.categories, name='categories'),
    path('categories/<int:subcategory_id>/', views.products_by_subcategory, name='products_by_subcategory'),

    path('products/', views.products, name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)