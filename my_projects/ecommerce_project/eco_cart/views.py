from django.shortcuts import render

# Create your views here.
def cart_detail(request):
    tempalte_name = 'cart/cart.html'
    return render(request,tempalte_name)