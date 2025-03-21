from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})  # ✅ Allow image selection
        }