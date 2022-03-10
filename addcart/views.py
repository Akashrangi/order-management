from genericpath import exists
from django.shortcuts import render,redirect,get_object_or_404
from auth_system.models import MyShopUsers
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import AddQuantityForm
from django.db.models import Q

# Create your views here.

def basket_detail(request):
    if MyShopUsers.objects.filter(username=request.user).exists():
        basket = Cart(request)
        for item in basket:
            item['update_quantity'] = AddQuantityForm(initial= {'quantity' : item['qty']})
    else:
        return redirect('login')
    
    return render(request, 'cart/cart.html', {'cart' : basket})

def basket_view(request,product_id):
    basket = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddQuantityForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product, qty=cd['quantity'])
    return redirect('carts')

@require_POST        
def basket_remove(request, product_id):
    basket = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    basket.delete(product)
    return redirect('carts') 

@require_POST
def basket_update(request, product_id):
    basket = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddQuantityForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        qty = cd['quantity']
        basket.update(product=product, qty=qty)
    return redirect('carts')     
        


