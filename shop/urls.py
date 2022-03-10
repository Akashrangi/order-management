from django.urls import path
from .import views
urlpatterns = [
    path('Your-Shop/',views.shop_view,name='shop'),
    path('Your-Shop/Create-Your-Product/',views.crete_product_view,name='create-product'),
    
]