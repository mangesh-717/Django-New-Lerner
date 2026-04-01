from django.urls import path
from _ree1app import views

app_name = "_ree1app"

urlpatterns=[
    path('',views.index,name='index'),
    path('display/',views.display,name='display'),
    path('contact/',views.contact,name='contact'),
    path('carrier/',views.carrier,name='carrier'),
    path('about/',views.about,name='about'),

]