from django.urls import path
from .import views

urlpatterns = [
    path('', views.useraccount, name="useraccount"),
    # path('orders', views.userorderhistory, name='userorderhistory'),
    path('orders', views.userorderhistory, name='userorderhistory'),
    path('addaddress', views.addaddress, name='useraddaddress'),
    path('updateaddress/<int:id>/', views.updateaddress, name='updateaddress'),
]