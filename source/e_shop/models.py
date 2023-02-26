from django.db import models


# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Еда'),
        ('clothes', 'Одежда'),
        ('other', 'Разное')
    ]
    product = models.CharField(max_length=100, verbose_name='Продукт')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    image = models.CharField(max_length=3000, verbose_name='Ссылка на фото')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name='Категория')
    remainder = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    class Meta:
        ordering = ['category', 'product']
        
    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES)[self.category]

    def __str__(self):
        return self.product
