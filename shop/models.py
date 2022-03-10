
from auth_system.models import MyShopUsers
from django.db import models

# Create your models here.
class Categorys(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    shop = models.ForeignKey(MyShopUsers,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    image = models.ImageField(max_length = 100)
    price = models.FloatField()
    def __str__(self):
        return f"{self.name}"

