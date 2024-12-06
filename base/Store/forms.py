from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "article", "brand", "description", "rating", "quantity"]
        
        
class SearchForm(forms.Form):
    query = forms.CharField()