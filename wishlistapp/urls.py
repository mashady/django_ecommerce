from django.urls import path
from .views import WishlistListCreateView, WishlistDeleteView

urlpatterns = [
    path('', WishlistListCreateView.as_view()),
    path('<int:pk>/', WishlistDeleteView.as_view()),
]
