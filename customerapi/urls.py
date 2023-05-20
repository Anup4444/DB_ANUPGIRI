from django.urls import path
from . import views

urlpatterns = [
    path('customer/create/', views.customer_create, name="create_customer"),
    path('customer/read/', views.customer_read, name="read_customer"),
    path('customer/update/', views.customer_update, name="update_customer"),
    path('customer/delete/', views.customer_delete, name="delete_customer"),
]
