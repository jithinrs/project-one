from django.contrib import admin
from .models import  Cart, Categories, Specification, SubCategory,Product, discount, wishlist, NewCart, NewCartItem
# Register your models here.

admin.site.register(Categories)
admin.site.register(SubCategory)


# class specAdmin(admin.TabularInline):
#     model = Specification
# class productAdmin(admin.ModelAdmin):
#     inlines = [specAdmin]



# admin.site.register(Product, productAdmin)
admin.site.register(Product)
admin.site.register(Specification)
admin.site.register(Cart)
admin.site.register(discount)
admin.site.register(wishlist)
# admin.site.register(Cartmodel) 


admin.site.register(NewCart)
admin.site.register(NewCartItem)