from rest_framework import serializers
from .models import CartItem
from productapp.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=CartItem.objects.all(), source='product', write_only=True
    )

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']
