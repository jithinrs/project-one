from django.urls import path
from .import views

urlpatterns = [
    path('', views.useraccount, name="useraccount"),
    path('orders', views.userorderhistory, name='userorderhistory')
]