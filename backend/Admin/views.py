from django.shortcuts import render,redirect
from .models import Book

from .serializers import BookSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,parser_classes         
from rest_framework.parsers import MultiPartParser,FormParser         
from rest_framework.response import Response                          
from rest_framework import status                                     


# Create your views here.


@api_view(['GET','POST'])                           
@parser_classes([MultiPartParser,FormParser])       
def book_details(request):
    if request.method=="GET":                                       
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":                                    
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def book_opns(request,bid):
    try:
        books=Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=BookSerializer(books)
        return Response(serializer.data)
    
    
    elif request.method=="PUT":
        serializer=BookSerializer(books,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method=="DELETE":
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)