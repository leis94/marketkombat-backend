"""Products models admin."""

# Django
from django.contrib import admin


# Models
from vsbuy_backend.products.models.products import Product
from vsbuy_backend.products.models.stores import Store
from vsbuy_backend.products.models.scraping_products import ScrapingProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""

    list_display = (
        'id',
        'name',
        'is_active'
    )

    search_fields = ('id', 'name')
    list_filter = (
        'is_active',
    )
    ordering = ('id',)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Store admin."""

    list_display = (
        'id',
        'name',
        'is_active'
    )

    search_fields = ('id', 'name')
    list_filter = (
        'is_active',
    )
    ordering = ('id',)