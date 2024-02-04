from rest_framework import serializers
from Admin.models import Book, Orders, Cart
from Admin.serializers import BookSerializer



#Used just to list books by their genres

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('id', 'book_title', 'book_author', 'book_genre','book_description','book_price','book_coverpage','book_publisher')
        
        


class MyOrderItemSerializer(serializers.ModelSerializer):    
    book = BookSerializer()

    class Meta:
        model = Cart
        fields = (
            "book",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = (
            "id",
            "address",
            "stripe_token",
            "items",
            "paid_amount"
        )

class OrderItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Cart
        fields = (
            "order",
            "book",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = (
            "id",
            "address",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Orders.objects.create(**validated_data)

        for item_data in items_data:
            Cart.objects.create(order=order, **item_data)
            
        return order