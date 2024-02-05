from django.urls import path
from Admin import views

urlpatterns = [
    path('books/',views.book_details,name="Books"),
    path('books/<int:bid>',views.book_opns,name="Books"),
    
]




