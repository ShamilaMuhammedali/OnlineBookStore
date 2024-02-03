from rest_framework import serializers
from Admin.models import Book


#Used just to list books by their genres

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('book_title', 'book_author', 'book_genre','book_description','book_price','book_coverpage','book_publisher')