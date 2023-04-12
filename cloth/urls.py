from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductListView.as_view(), name='Product'),
    path('product/<int:id>', views.ProductDetailView.as_view(), name='ProductDetail'),
]