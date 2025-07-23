# forms/mstd_forms.py
from django import forms
from ..models.master import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'theoritical_yield_pcs', 'target_yield_percent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'theoritical_yield_pcs': forms.NumberInput(attrs={'class': 'form-control'}),
            'target_yield_percent': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }