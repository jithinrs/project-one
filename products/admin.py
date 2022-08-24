from django.contrib import admin
from .models import Categories, SubCategory,Product
# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(Product)