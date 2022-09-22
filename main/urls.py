from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views as view


urlpatterns = [
    path('login', views.Login),
    path('create_user', views.createUser)
    
]