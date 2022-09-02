from email import message

from turtle import title
from unicodedata import category
from xml.dom import ValidationErr
from django.db import models
from django.urls import reverse

# Create your models here.

# class TitleManager(models.Manager):
#     def Validate(self, title):
#         x = title.title()
#         catgeory = Categories.objects.create(
#             title = x
#         )
            # error_messages = { "unique":"The Geeks Field you entered is not unique."}


class Categories(models.Model):
    id =  models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=255, unique=True)
    url_slug = models.CharField(max_length=255, unique=True)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # objects = TitleManager()

    class Meta():
        verbose_name_plural = "Categories"
        # unique_together = [['title']]

    # def save(self, force_insert=False, force_update=False):
    #     self.title = self.title.title() 
    #     super(Categories, self).save(force_insert, force_update)

    # def clean(self):
    #     cleaned_data = self.cleaned_data['title']
    #     print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     if Categories.objects.filter(title = title).exists():
    #         raise ValidationErr('please enter another name')

    # def save(self, *args, **kwargs):
    #     try:
    #         self.title = self.title.title()
    #         return super().save(*args, **kwargs)
    #     except:
    #         return 

            


    def get_absolute_url(self): 
        return reverse('categorylist')

    def __str__(self):
        return self.title

# def clean(self):
#     cleaned_data = super(Categories,self).clean()
#     print(cleaned_data)
#     title = cleaned_data.get('title')
#     if Categories.objects.filter(title = title).exists():
#         raise ValueError('please enter another name')

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('subcategoryfulllist')

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.SlugField(max_length=255)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategories_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_image = models.FileField()
    product_image_1 = models.FileField(default='')
    product_image_2 = models.FileField(default='')
    product_image_3 = models.FileField(default='')
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock_total = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self): 
        return reverse('productlist')
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

class Cartmodel(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
