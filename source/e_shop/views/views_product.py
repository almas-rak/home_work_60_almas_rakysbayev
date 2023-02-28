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
        product = Product.objects.create(**form.cleaned_data)
        return redirect('detail_view', pk=product.pk)
    return render(request, 'add_product.html', context={'form': form})


def edit_product(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'edit_product.html', context={'form': form, 'product': product})
    else:
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail_view', pk=pk)
        else:
            return render(request, 'update_product.html', context={'form': form})


def delete_product(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'detail_product.html', context={'product': product, 'delete': 'delete'})
    else:
        product.delete()
        return redirect('home')


def detail_view(request: WSGIRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_product.html', context={'product': product})
