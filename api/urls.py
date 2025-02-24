from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets import UsuarioViewSet, JogoViewSet
from .views import GetQtdLikes, GetLikes

rotas = routers.DefaultRouter()
rotas.register(r'usuarios', UsuarioViewSet)
rotas.register(r'jogos', JogoViewSet)

urlpatterns = [
    path("", include(rotas.urls)),
    path('GetQtdLikes/<int:id_jogo>/', GetQtdLikes, name="GetQtdLikes"),
    path('GetLikes/<int:id_jogo>/', GetLikes, name="GetLikes"),
    path('api-rest/', include('rest_framework.urls')),
]
