from django.shortcuts import render,redirect

from Admin.models import Book

from .serializers import GenreSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view,parser_classes         
from rest_framework.parsers import MultiPartParser,FormParser         
from rest_framework.response import Response                          
from rest_framework import status          

# Create your views here.


@api_view(['GET'])
def postBookByGenre(request, genreSearch):
    book = Book.objects.filter(book_genre=genreSearch)
    serializer = GenreSerializer(book, many=True)
    return Response(serializer.data)