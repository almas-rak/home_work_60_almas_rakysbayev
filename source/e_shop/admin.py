from django.contrib import admin

from e_shop.models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'description', 'image', 'category', 'remainder', 'price', 'is_deleted',
                    'deleted_at')
    list_editable = ('product', 'description', 'category', 'remainder', 'price', 'is_deleted')


admin.site.register(Product, ProductAdmin)
