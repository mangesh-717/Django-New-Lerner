from django.contrib import admin
from django.urls import path,include
from .views import *

# to register api we use as_view in order to register model view set we need different kind of machenisam thats called router
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'students',StudentViewset,basename="students")
urlpatterns=router.urls


urlpatterns = [
# in order to register router in path 
    path('students/',include(router.urls)),

    path('', index_ ),
    # path('your-model/', YourModelAPIView.as_view(), name='your-model-api'),
    path('student/',serializedatudent)


    # its apiview calling
    ,path('persons/',PersonApi.as_view())
]

























# when we perform custom methods means actions in model view set 
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewset

# router = DefaultRouter()
# router.register(r'students', StudentViewset, basename='students')

# urlpatterns = [
#     # ... other URL patterns ...
#     path('students/<int:pk>/custom-action/', StudentViewset.as_view({'get': 'custom_action'}), name='custom-action'),
#     path('students/', include(router.urls)),
# ]
