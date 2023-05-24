from django.urls import path

from main.views import contacts, index


urlpatterns = [
    path('', index),
    path('contacts/', contacts, name='contacts'),
]