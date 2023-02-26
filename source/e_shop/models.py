from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Описание')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category


class ChildCategory(models.Model):
    category = models.CharField(max_length=100, verbose_name='Категория')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    parent = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name='Родительская категория')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.category


class Product(models.Model):
    product = models.CharField(max_length=100, verbose_name='Продукт')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    image = models.CharField(max_length=3000, verbose_name='Ссылка на фото')
    category = models.ForeignKey(ChildCategory, on_delete=models.RESTRICT, verbose_name='Категория')
    remainder = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.product
