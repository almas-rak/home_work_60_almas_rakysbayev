from django.urls import path

from e_shop.views.views_product import IndexView, CreateProductView, UpdateProductView, DetailProductView, \
    ProductDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add/product/', CreateProductView.as_view(), name='create_product'),
    path('edit/product/<int:pk>', UpdateProductView.as_view(), name='edit_product'),
    path('delete/product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('detail/view/<int:pk>', DetailProductView.as_view(), name='detail_view'),

]
