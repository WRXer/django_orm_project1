from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from transliterate import translit

from config import settings

NULLABLE = {'blank': True, 'null': True}



class Category(models.Model):
    name = models.CharField(max_length=255)    #наименование,
    description = models.TextField()    #описание.

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Category"     # наименование модели в единственном числе
        verbose_name_plural = "Categories"     # множественное число наименования модели

class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="user__name")
    email = models.CharField(max_length=100, verbose_name="user_email")
    message = models.CharField(max_length=100, verbose_name="user_message")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class Product(models.Model):
    name = models.CharField(max_length=255)    #наименование
    description = models.TextField()    #описание,
    image = models.ImageField(upload_to='products/', **NULLABLE)    #изображение (превью),
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    #категория,
    price = models.DecimalField(max_digits=10, decimal_places=2)     #цена за покупку,
    created_at = models.DateTimeField(default=timezone.now)    #дата создания,
    recreated_at = models.DateTimeField(auto_now=True)    #дата последнего изменения.
    is_active = models.BooleanField(default=True, verbose_name='активно')
    product_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.image}\n{self.name} {self.description}'

    def get_active_version(self):
        return Version.get_active_version(self)

    class Meta:
        verbose_name = "Product"   # наименование модели в единственном числе
        verbose_name_plural = "Products"    # множественное число наименования модели



class Blogs(models.Model):
    name = models.CharField(max_length=100, verbose_name="blog_name")    #заголовок
    description = models.TextField(null=True, blank=True, verbose_name="blog_description")    #содержимое
    image = models.ImageField(upload_to='products/', **NULLABLE)    #превью (изображение)
    created_at = models.DateTimeField(default=timezone.now)    #дата создания
    is_published = models.BooleanField(default=True)    #признак публикации
    blog_views = models.IntegerField(verbose_name="blog_views", default=0)    #количество просмотров
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Blogs, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    # def delete(self, *args, **kwargs):
    #     self.is_published = False
    #     self.save()
    def get_absolute_url(self):
        return reverse('main:blog_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Blog"    # наименование модели в единственном числе
        verbose_name_plural = "Blogs"    # множественное число наименования модели


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - {self.version_number} "

    def save(self, *args, **kwargs):
        if self.is_active:  # Деактивируем все другие версии для данного продукта
            Version.objects.filter(product=self.product).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_version(cls, product):
        try:
            return cls.objects.get(product=product, is_active=True)
        except ObjectDoesNotExist:
            return None