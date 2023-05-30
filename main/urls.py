from django.urls import path

from main.apps import MainConfig
from main.views import ContactCreateView, IndexListView, ProductsDetailView, BlogsListView, ProductsListView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name= 'index'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('product_details/<int:pk>/', ProductsDetailView.as_view(), name='product_details'),
    path('blogs/', BlogsListView.as_view(), name= 'blogs')
]
