"""Product URLs."""

#Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from vsbuy_backend.products.views import products as product_views
from vsbuy_backend.products.views import stores as store_views
from vsbuy_backend.products.views import scraping_products as scrap_views

router = DefaultRouter()
router.register(r'products', product_views.ProductViewSet, basename='product')
router.register(r'stores', store_views.StoreViewSet, basename='store')
router.register(r'scrap', scrap_views.ScrapingProductViewSet, basename='scrap')

urlpatterns = [
    path('', include(router.urls))
]