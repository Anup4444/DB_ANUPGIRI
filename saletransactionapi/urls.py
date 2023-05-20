from django.urls import path
from . import views

urlpatterns = [
    path('saletransaction/create/', views.saletransaction_create, name="create"),
    path('saletransaction/read/', views.saletransaction_read, name="read"),
    path('saletransaction/update/', views.saletransaction_update, name="update"),
    path('saletransaction/delete/', views.saletransaction_delete, name="delete"),
]
