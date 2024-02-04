from django.db import models
from django.contrib.auth.models import User    


# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length = 100)
    book_genre = models.CharField(max_length = 100)
    book_description = models.TextField()
    book_price = models.IntegerField()
    book_coverpage = models.FileField(upload_to= "coverpages/")
    book_author = models.CharField(max_length = 100)
    book_year = models.IntegerField()
    book_publisher = models.CharField(max_length = 100)
    book_stock = models.CharField(max_length = 100)
    book_status = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.book_title
        
        
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    order_date = models.DateField(auto_now=True)
    order_status = models.IntegerField(default=0)
    stripe_token = models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    
    
    class Meta:
        ordering = ['-order_date',]
    
    
    
class Cart(models.Model):
    order = models.ForeignKey(Orders, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    cart_status = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    



