from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from e_shop.forms import ProductForm
from e_shop.models import Product


def index_view(request: WSGIRequest):
    products = Product.objects.filter(remainder__gt=0)
    return render(request, 'index.html', context={'products': products})


def create_product(request: WSGIRequest):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', context={'form': form})
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_product.html', context={'form': form})

