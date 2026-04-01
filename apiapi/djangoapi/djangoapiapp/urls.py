from django.urls import path,include

from .views import CompanyviewSet,CustomAuthToken
from rest_framework.routers import *

router=DefaultRouter()
router.register(r'companies',CompanyviewSet)
urlpatterns=router.urls
# this is default router
urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),


]
