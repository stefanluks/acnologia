from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import UsuarioViewSet, JogoViewSet

rotas = routers.DefaultRouter()
rotas.register(r'usuarios', UsuarioViewSet)
rotas.register(r'jogos', JogoViewSet)

urlpatterns = [
    path("", include(rotas.urls)),
    path('api-rest/', include('rest_framework.urls')),
]
