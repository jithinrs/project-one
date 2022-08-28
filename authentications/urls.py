from django.urls import path
from .import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('verify/', views.verify_code ,name='verify'), 
]