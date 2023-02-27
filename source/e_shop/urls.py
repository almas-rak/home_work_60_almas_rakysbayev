from django.urls import path

from e_shop.views.views_product import index_view, create_product, edit_product, delete_product, detail_view

urlpatterns = [
    path('', index_view, name='home'),
    path('add/product/', create_product, name='create_product'),
    path('edit/product/<int:pk>', edit_product, name='edit_product'),
    path('add/product/<int:pk>', delete_product, name='delete_product'),
    path('detail/view/<int:pk>', detail_view, name='detail_view'),

]
