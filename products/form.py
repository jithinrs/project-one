from django import forms
from .models import Categories
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        