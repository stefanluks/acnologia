from .models import Jogo, Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"