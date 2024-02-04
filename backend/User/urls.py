from django.urls import path
from User import views

urlpatterns = [
    path('searchbygenre/<str:genreSearch>', views.postBookByGenre, name="SearchBook"),
    path('addtocart/<int:bid>',views.add_to_cart,name="AddToCart"),
    path('checkout/', views.checkout, name="Checkout"),
    path('orders/', views.OrdersList.as_view()),  
    
]