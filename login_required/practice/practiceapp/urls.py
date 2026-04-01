from django.urls import path
from .views import index,login_form,result
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('index/',index,name='index'),
    path('',login_form,name='login'),
    path('result/',result,name='result')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
