from django.db import models
from django.conf import settings
from productapp.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:# handle unique
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user.email} - {self.product.name} x {self.quantity}"
