from django.shortcuts import render,get_object_or_404
import random
from django.db.models import Q

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


def category(request,category_slug):
    template_name = 'product/category.html'
    category = get_object_or_404(Category, slug=category_slug)

    return render(request,template_name,{'category':category})



#search
def search(request):
    query = request.GET.get('q','')
    products = Product.objects.filter(Q(title__icontains=query)| Q(description__icontains=query))

    template_name = 'product/search.html'
    return render(request,template_name,{'products':products,'query':query})