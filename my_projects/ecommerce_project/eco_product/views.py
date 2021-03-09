from django.shortcuts import render,get_object_or_404
import random

# Create your views here.
from .models import Category,Product

def productDetail(request,category_slug,product_slug):
    product = get_object_or_404(Product,category__slug=category_slug,slug =product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if (len(similar_products)>4):
        similar_products = random.sample(similar_products,4)
    
    template_name = 'product/product.html'
    context = {
        'product':product,
        'similar_products':similar_products,
    }
    return render(request,template_name,context)

    