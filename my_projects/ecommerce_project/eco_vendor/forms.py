from ecommerce_project.eco_product.models import Category,Product
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','image','title','description','price']