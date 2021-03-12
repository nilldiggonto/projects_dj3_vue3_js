from django.shortcuts import render,redirect
from .cart import Cart

# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    tempalte_name = 'cart/cart.html'
    remove_from_cart = request.GET.get('remove_from_cart','')
    change_quantity = request.GET.get('change_quantity','')
    quantity = request.GET.get('quantity',0)
    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('eco-cart')

    if change_quantity:
        cart.add(change_quantity,quantity,True)

        return redirect('eco-cart')
    return render(request,tempalte_name)