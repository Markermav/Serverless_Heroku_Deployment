from os import stat
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import Product, Mobile
from rest_framework import viewsets

# Create your views here.


@api_view(['GET'])
def home(request):
    return Response({
        'message': 'Everything working fine' 
    }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_mobiles(request):
    mobiles = Mobile.objects.all()
    serializer = MobileSerializer(mobiles, many=True)
    return Response(serializer.data)  


class FoodView(viewsets.ModelViewSet):
    queryset  = Food.objects.all()
    serializer_class  = FoodSerializer


@api_view(['POST'])
def post_Product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message':'Product Creation failed'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def product_details(request, id):
    try:
        p = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        productserializer = ProductSerializer(p)
        return Response(productserializer.data)

    elif  request.method == 'PUT':
        serializer =  ProductSerializer(p, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response({'message': 'Item Deleted'}, status=status.HTTP_200_OK)