from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'id_categoria', 'description', 'marca', 'image', 'priceUSD', 'code', 'productCode')

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = ('id', 'name')
        
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    pedidos = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'