from .models import *
from rest_framework import viewsets, permissions
from django_filter.rest_framework import DjangoFilterBackend
from .serializers import *
from rest_framework.response import Response
from rest_framework import status   

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                            statis=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer