from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer