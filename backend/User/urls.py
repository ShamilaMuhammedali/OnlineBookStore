from django.urls import path
from User import views

urlpatterns = [
    path('searchbygenre/<str:genreSearch>', views.postBookByGenre),
    
]