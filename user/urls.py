from django.urls import path
from user.views import RegistroUsuario

urlpatterns = [
     path('new/',RegistroUsuario.as_view(),name = ''),
]