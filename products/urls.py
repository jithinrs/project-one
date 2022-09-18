from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/', views.adminbase,name='adminbase'),
    path('categorylist/', views.Categorylist.as_view(), name='categorylist'),
    path('categoryadd/', views.Categoryadd.as_view(), name='categoryadd'),
    path('category_delete/<int:id>/', views.category_delete, name='category_delete'),
    path('category_update/<slug:pk>/', views.Categoryupdate.as_view(), name='category_update'),
    path('subcategorylist/<int:id>/', views.SubCategorylist.as_view(), name='subcategorylist'),
    path('subcategorylist', views.SubCategoryFullList.as_view(), name='subcategoryfulllist'),
    path('subcategoryadd/', views.SubCategoryadd.as_view(), name='subcategoryadd'),
    path('subcategory_update/<slug:pk>/', views.SubCategoryupdate.as_view(), name='subcategory_update'),
    path('subcategory_delete/<int:id>/', views.subcategory_delete, name='subcategory_delete'),
    path('productlist/', views.Productlist.as_view(), name='productlist'),
    path('productadd/', views.Productadd.as_view(), name='productadd'),
    path('productspec/', views.Productspec.as_view(), name='productspec'),
    path('product_update/<slug:pk>/', views.Productupdate.as_view(), name='product_update'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    path('orderlist/', views.adminorder, name='orderlist'),
]