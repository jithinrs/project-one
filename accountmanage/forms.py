from django import forms
from .models import useraddress


class addressform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Name'}))
    address_1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = useraddress
        fields = ['name', 'address_1', 'address_2', 'city', 'district', 'state', 'pincode']
    