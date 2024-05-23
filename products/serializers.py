from rest_framework import serializers
from models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'id_categoria', 'description', 'marca', 'image', 'priceUSD', 'code', 'productCode')