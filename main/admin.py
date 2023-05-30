from django.contrib import admin

from main.models import Product, Category, Blogs


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at", "blog_views")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("created_at",)