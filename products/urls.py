from rest_framework import routers
from views import *

router = routers.DefaultRouter()


router.register('api/products', ProductViewSet, 'products')

urlpatterns = router.urls

# 16:46