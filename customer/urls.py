from django.urls import path

from . import views

urlpatterns = [
    path('customer/',views.customer_view,name='customer'),
    path('customer/<int:id>/Product-Detail/',views.product_detail_view,name='product-detail'),
    path('search/',views.search,name='serching'),
    path('All-Products/',views.all_products,name='All'),
]