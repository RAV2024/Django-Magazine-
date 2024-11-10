from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)