from django.urls import path
from . import views

urlpatterns = [
    path('invoice/create/', views.invoice_create, name="create_invoice"),
    path('invoice/read/', views.invoice_read, name="read_invoice"),
    path('invoice/update/', views.invoice_update, name="update_invoice"),
    path('invoice/delete/', views.invoice_delete, name="delete_invoice"),
]
