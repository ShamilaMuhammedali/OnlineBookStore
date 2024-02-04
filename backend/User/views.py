from django.shortcuts import render,redirect

from Admin.models import Book, Orders, Cart

from .serializers import GenreSerializer, MyOrderItemSerializer, MyOrderSerializer, OrderItemSerializer, OrderSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes         
from rest_framework.parsers import MultiPartParser,FormParser         
from rest_framework.response import Response                          
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from django.http import Http404

import stripe
from django.conf import settings

from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User   


# Create your views here.


@api_view(['GET'])
def postBookByGenre(request, genreSearch):
    book = Book.objects.filter(book_genre=genreSearch)
    serializer = GenreSerializer(book, many=True)
    return Response(serializer.data)




@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('book').price for item in serializer.validated_data['items'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='AED',
                description='Charge from Book Bound',
                source=serializer.validated_data['stripe_token']
            )

            user_token = Token.objects.get(user=request.user)
            user = User.objects.get(id=user_token)
            serializer.save(user=user, paid_amount=paid_amount)
            
            for item in serializer.validated_data['items']:
                book = item.get('book')
                bookdata = Book.objects.get(id=book)
                bookdata.book_stock = bookdata.book_stock - item.get('quantity')
                bookdata.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Orders.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)