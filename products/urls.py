from django.urls import path
from rest_framework import routers
from . import views
from .flow_utils import *

router = routers.DefaultRouter()
router.register('api/products', views.ProductViewSet, 'products')
router.register('api/categories', views.CategoryViewSet, 'categories')
router.register('api/pedidos', views.PedidoViewSet, 'pedidos')
router.register('api/detalle', views.DetallePedidoViewSet, 'detalle')

urlpatterns = router.urls + [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
    path('api/create-payment/', create_payment, name='create_payment'),

]
