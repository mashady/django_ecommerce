from rest_framework import serializers
from .models import Product
from categoryapp.serializers import CategorySerializer
from categoryapp.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'cover', 'category', 'category_id']
