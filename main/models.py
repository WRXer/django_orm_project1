from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=255)    #наименование,
    description = models.TextField()    #описание.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Category"     # наименование модели в единственном числе
        verbose_name_plural = "Categories"     # множественное число наименования модели

class Product(models.Model):
    name = models.CharField(max_length=255)    #наименование
    description = models.TextField()    #описание,
    image = models.ImageField(upload_to='products/', **NULLABLE)    #изображение (превью),
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    #категория,
    price = models.DecimalField(max_digits=10, decimal_places=1)     #цена за покупку,
    created_at = models.DateTimeField(default=timezone.now)    #дата создания,
    recreated_at = models.DateTimeField(auto_now=True)    #дата последнего изменения.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Product"   # наименование модели в единственном числе
        verbose_name_plural = "Products"    # множественное число наименования модели