from django.db import models
from product import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(user , on_delete=models.CASCADE , related_name='carts')
    is_paid = models.BooleanField(default=False)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL , null=True , blank=True)
    