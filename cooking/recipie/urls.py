from django.urls import path  
from recipie.views import pizza
from recipie.views import burger
from recipie.views import noodles
from recipie.views import sandwich
from recipie.views import gravy
from recipie.views import soup
urlpatterns = [  
    path('piz/',pizza)  ,
    path('bur/',burger) ,
    path('no/',noodles) ,
    path('sand/',sandwich),
    path('grav/',gravy),
    path('soup/',soup)
    
]  
