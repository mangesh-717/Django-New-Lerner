from django.urls import path
from p1 import views
urlpatterns = [
    path('',views.index,name='indexhome'),
    path('result/',views.result , name="resulthome")
]