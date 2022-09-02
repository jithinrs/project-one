from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('<slug:url_slug>/', views.SingleProView, name='productview'),
    path('cart/',views.cart,name='cart')
    
]