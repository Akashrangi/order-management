from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index_view,name='index'),
    path('Register/',views.register_view,name='register'),
    path('Login/',views.login_view,name='login'),
    path('Logout/',views.logout_view,name='logout'),
]