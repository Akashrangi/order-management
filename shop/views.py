
from django.shortcuts import redirect, render
from .models import Product
from auth_system.models import MyShopUsers
from .forms import ProductForm

# Create your views here.
def shop_view(request):
    product = Product.objects.filter(shop=request.user)
    context = {
        'product':product
    }
    return render(request,'shop/shop.html',context)

def crete_product_view(request):
    form = ProductForm()
    user = request.user
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get('image')
            cd= MyShopUsers.objects.get(pk=request.user.id)
            user = form.save(commit=False)
            user.shop = cd
            user.image = img
            user.save()
            return redirect('shop')
    return render(request,'shop/create_product.html',{'form':form})

