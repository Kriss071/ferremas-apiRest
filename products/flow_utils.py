import hashlib
import hmac
from django.urls import reverse
import requests
from rest_framework.decorators import api_view
from .serializers import *
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


def sign_request(params):
    keys = sorted(params.keys())
    to_sign = ''.join(key + str(params[key]) for key in keys)
    signature = hmac.new(bytes(settings.FLOW_SECRET_SANDBOX, 'utf-8'), to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

def make_request(url, params, method='GET'):
    signature = sign_request(params)
    params['s'] = signature

    if method == 'GET':
        response = requests.get(url, params=params)
    else:
        response = requests.post(url, data=params)
    return response.json()


@api_view(['POST'])
def create_payment(request):
    if request.method == 'POST':
        serializers = PedidoSerializer(data=request.data)
        
        if serializers.is_valid():
            data = serializers.validated_data
        
            url = 'https://sandbox.flow.cl/api/payment/create'
            
            url_return = 'http://127.0.0.1:8000/retorno_flow/'
            url_confirmation = 'http://127.0.0.1:8000/catalogo/'
            
            params = {
                'apiKey': settings.FLOW_KEY_SANDBOX,
                'commerceOrder': f"F{data['nombre']}" ,
                'subject': 'Pago de pruebA',
                'currency': 'CLP',
                'amount': data['valor_total'],
                'email': data['correo'],
                "urlConfirmation": url_confirmation,
                "urlReturn": url_return,
            }
             
            print("Parámetros para crear el pago:", params)

            response = make_request(url, params, method='POST')

            return Response(response)

        return Response({'msg': 'Datos no recibidos', 'data': data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_payment(request):
    url = 'https://sandbox.flow.cl/api/payment/getStatus'
    data = request.data
    print('===== DATA ====')
    print(data)
    
    parametros = {
        'apiKey': settings.FLOW_KEY_SANDBOX,
        'token': data,
    }
    
    response = make_request(url, parametros, method='GET')
    
        
    transaccion = {
        'commerceOrder': response.get('commerceOrder'),
        'requestDate': response.get('requestDate'),
        'subject': response.get('subject'),
        'payer': response.get('payer'),
        'amount': response.get('amount'),
        'currency': response.get('currency'),
        'media': response.get('paymentData', {}).get('media'),
        'status': response.get('status')
    }
    
    print(transaccion)
    
    return Response(transaccion)
