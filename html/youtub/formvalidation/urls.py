from django.urls import path
from formvalidation import views
urlpatterns = [
    path('',views.employee_form),
    path('list/',views.employee_list,name='_list'),
    path('delete-list/<id>/',views.employee_delete,name='employee_delete'),



    path('employee_update/<id>/',views.updation_data,name='employee_update')
]
# 
# list/base.html
# list/delete-base
# /list/


# /list/