from django.shortcuts import redirect, render
from .models import MyShopUsers
from .forms import MyShopUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_ ,logout
from shop.models import Product
from addcart.forms import AddQuantityForm


# Create your views here.

def index_view(request):
    products = Product.objects.all()
    form = AddQuantityForm()
    return render(request,'auth_system/index.html',{'products':products,'form':form})

def register_view(request):
    form = MyShopUserForm()
    if request.method == 'POST':
        form = MyShopUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render (request,'auth_system/Register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user:
            login_(request,user)
            if user.user_type == 'Seller':
                return redirect('shop')
            else:
                return redirect('customer')
        else:
            messages.error(request,'invalid')
            return redirect('login')


    return render (request,'auth_system/Login.html')

def logout_view(request):
    logout(request)
    return redirect('index')
