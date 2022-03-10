from shop.models import Product
from addcart.forms import AddQuantityForm
from django.shortcuts import render

# Create your views here.
def customer_view(request):
    products = Product.objects.all()[:3]
    
    form = AddQuantityForm()
    return render(request,'customer/customer.html',{'products':products,'form':form})

def all_products(request):
    products = Product.objects.all()
    form = AddQuantityForm()
    return render(request,'customer/products.html',{'pr':products,'form':form})

def product_detail_view(request,id):
    details = Product.objects.get(pk=id)
    cart_product_form = AddQuantityForm()
    context = {
        'details' : details,
        'cart_product_form' : cart_product_form
    }
    return render(request,'customer/product_detail.html',context)

def search(request):        
    if request.method == 'GET':      
        pname =  request.GET.get('search') 
        try:
            status = Product.objects.filter(name__icontains=pname) 
            return render(request,"customer/search.html",{"product":status})
        except:
            pass
    else:
        return render(request,"search.html",{})