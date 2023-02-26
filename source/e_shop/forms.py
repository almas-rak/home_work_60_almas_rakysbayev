from django import forms

from e_shop.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product', 'description', 'image', 'category', 'remainder', 'price')
