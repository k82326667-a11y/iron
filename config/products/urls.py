from django.urls import path
from .views import ProductListCreateAPIView  # берем ListCreateAPIView

urlpatterns = [
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
]
