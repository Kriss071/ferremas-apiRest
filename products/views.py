from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer