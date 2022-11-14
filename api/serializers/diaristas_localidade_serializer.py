from dataclasses import fields
from rest_framework import serializers
from ..models import Usuario

class DiaristasLocalidadesSerializers(serializers.ModelSerializer):
    cidade = serializers.SerializerMethodField()
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'reputacao', 'foto_usuario', 'cidade')
        
    def get_cidade(self, obj):
        return "São Paulo"