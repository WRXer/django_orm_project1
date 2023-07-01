from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ContactCreateView, IndexListView, ProductsDetailView, BlogsListView, ProductsListView, \
    BlogsDetailView, BlogsCreateView, BlogsDeleteView, BlogsUpdateView, ProductsCreateView, ProductsUpdateView, \
    ProductsDeleteView

app_name = MainConfig.name




urlpatterns = [
    path('', IndexListView.as_view(), name= 'index'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', cache_page(60)(ProductsListView.as_view()), name='products'),
    path('product_detail/<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductsCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductsUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductsDeleteView.as_view(), name='product_delete'),
    path('blogs/', BlogsListView.as_view(), name= 'blogs'),
    path('blog_detail/<int:pk>/', BlogsDetailView.as_view(), name='blog_detail'),
    path('blogs/create/', BlogsCreateView.as_view(), name='create_blogs'),
    path('blogs/update/<int:pk>/', BlogsUpdateView.as_view(), name='update_blogs'),
    path('blogs/delete/<int:pk>/', BlogsDeleteView.as_view(), name='delete_blogs'),

]
