from django.urls import path

from main.apps import MainConfig
from main.views import ContactCreateView, IndexListView, ProductsDetailView, BlogsListView, ProductsListView, \
    BlogsDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name= 'index'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product_detail/<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
    path('blogs/', BlogsListView.as_view(), name= 'blogs'),
    path('blog_detail/<int:pk>/', BlogsDetailView.as_view(), name='blog_detail'),
]
