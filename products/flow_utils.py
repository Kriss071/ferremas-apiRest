from rest_framework.decorators import api_view
from .serializers import *
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_payment(request):
    if request.methos == 'POST':
        serializers = PedidoSerializer(data=request.data)
        
        if serializers.is_valid():
            data = serializers.validated_data
        
            url = 'https://sandbox.flow.cl/api/payment/create'
            print(data)
            #  params = {
            #     'apiKey': settings.FLOW_KEY_SANDBOX,
            #     'commerceOrder': f"F{id_pedido}" ,
            #     'subject': 'Pago de pruebA',
            #     'currency': 'CLP',
            #     'amount': monto,
            #     'email': email,
            #     "urlConfirmation": url_confirmation,
            #     "urlReturn": url_return,
            # }
            return Response({'msg': 'Datos recibidos', 'data': data}, status=status.HTTP_200_OK)
        