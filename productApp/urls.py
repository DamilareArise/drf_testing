from django.urls import path
from .views import ProductView

urlpatterns = [
    path("product/", ProductView.as_view(), name='product-list-create'),
    path("product/<int:prd_id>/", ProductView.as_view(), name='product-update')
]
