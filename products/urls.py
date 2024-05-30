from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('api/products', views.ProductViewSet, 'products')
router.register('api/categories', views.CategoryViewSet, 'categories')

urlpatterns = router.urls + [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
