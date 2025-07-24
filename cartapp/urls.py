from django.urls import path
from .views import CartListCreateAPIView, CartItemUpdateDeleteAPIView

urlpatterns = [
    path('cart/', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartItemUpdateDeleteAPIView.as_view(), name='cart-item-detail'),
]
