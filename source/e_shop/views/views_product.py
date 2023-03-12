from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from e_shop.forms import ProductForm
from e_shop.models import Product


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        query = Product.objects.filter(remainder__gt=0, is_deleted=False).order_by('category', 'product')
        return query


class CreateProductView(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('detail_view', kwargs={'pk': self.object.pk})


class UpdateProductView(UpdateView):
    template_name = 'edit_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('detail_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'detail_product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        context['delete'] = 'delete'
        return context

    def get_success_url(self):
        return reverse('home')


class DetailProductView(DetailView):
    template_name = 'detail_product.html'
    model = Product
