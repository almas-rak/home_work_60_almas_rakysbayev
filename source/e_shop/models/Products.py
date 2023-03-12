from django.db import models
from django.utils import timezone


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
    is_deleted = models.BooleanField(default=False, null=True, verbose_name='Удалено')
    deleted_at = models.DateTimeField(null=True, verbose_name='Дата и время удаления')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES)[self.category]

    def __str__(self):
        return self.product
