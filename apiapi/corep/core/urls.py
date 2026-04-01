from django.urls import path,include

from .views import *
urlpatterns = [
    path('', home),
    path('postview/', Post_view),
   
]
