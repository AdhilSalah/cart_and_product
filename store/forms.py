from dataclasses import fields
from django.forms import ModelForm
from .models import Products

class ProductForm(ModelForm):

    class Meta:
        model = Products
        fields = ['product_name','price','image']