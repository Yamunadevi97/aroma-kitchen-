from django.urls import path  
from suggestion.views import suggestion 

urlpatterns = [  
    path('sug/', suggestion), 

       
]  
