from django.urls import path
from . import views

urlpatterns = [
    path('product/create/', views.product_create, name="product"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
