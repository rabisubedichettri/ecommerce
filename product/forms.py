# forms.py
from django import forms
from .models import ProductCategory,Product,ProductImage
from django.forms import modelformset_factory

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name',]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'category', 'model_number', 
            'stock', 'price', 'featured_image', 'description', 
            'specifications'
        ]


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['name', 'image']




