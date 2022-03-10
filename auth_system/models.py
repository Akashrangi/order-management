from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_CHOICES = (
    ('Seller','Seller'),
    ('Customer','Customer'),
)


class MyShopUsers(AbstractUser):
    contact = models.CharField(max_length=10,default='+91')

    user_type = models.CharField(choices=USER_CHOICES,max_length=20,default='Customer')
    
    def __str__(self):
        return f"{self.username}"