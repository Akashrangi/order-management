from . import views
from django.urls import path

urlpatterns = [
    path('',views.basket_detail,name='carts'),
    path('add/<int:product_id>/',views.basket_view,name='cart_add'),
    path('remove/<int:product_id>/', views.basket_remove, name='basket_remove'),
    path('update/<int:product_id>/', views.basket_update, name='basket_update'),
]