from django.urls import path
from new1app.views import *
urlpatterns = [
    path('add_info/',index,name="index"),
    path('',login_form,name="login"),
    path('register/',register_form,name="registerHome"),
    path('result/',result,name="result"),

    path('update_student/<id>/',update,name="update_student"),
    path('delete_student/<id>/',delete,name="delete_student"),
]