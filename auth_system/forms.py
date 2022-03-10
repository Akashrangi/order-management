from .models import MyShopUsers
from django.contrib.auth.forms import UserCreationForm

class MyShopUserForm(UserCreationForm):
    class Meta:
        model = MyShopUsers
        fields = ('username','email','contact','user_type','password1','password2')