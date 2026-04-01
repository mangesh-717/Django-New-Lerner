from django.urls import path
from p6 import views
urlpatterns = [
    path('',views.index,name='index.home'),
    path('result/',views.result , name='result.home'),
    path('updation/',views.updation , name='updation.home'),
    path('deletion/',views.deleation , name='result.home'),
]