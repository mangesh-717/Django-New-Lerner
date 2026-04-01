from django.urls import path
from additionhtmlapp import views

urlpatterns = [
    path('',views.index),
    path('result', views.result),
]