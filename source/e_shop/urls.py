from django.urls import path

from e_shop.views.views_product import index_view

urlpatterns = [
    path('', index_view, name='home'),

]
