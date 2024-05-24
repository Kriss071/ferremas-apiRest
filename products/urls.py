from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register('api/products', ProductViewSet, 'products')
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls

