from django.urls import path
from . import views

urlpatterns = [
    path('get_customer_info/', views.get_customer_info, name="get_customer_info")

]
