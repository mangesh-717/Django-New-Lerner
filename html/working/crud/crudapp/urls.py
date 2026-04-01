from django.urls import path
from crudapp import views
urlpatterns = [
    path('',views.index,name='indexhome'),
    path('result/',views.result , name="resulthome"),

]

# utils.py

