from django import forms
from .models import Categories, Product, SubCategory
# class ProductCreateForm(forms.ModelForm):
#     class Meta:
#         model = Categories
        
class ProductsAddforms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategories_id'].queryset = SubCategory.objects.none()