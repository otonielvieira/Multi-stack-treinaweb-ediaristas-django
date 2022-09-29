from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadesSerializers
from rest_framework import status as status_http


class DiasristasLocalidades(APIView):
    def get(self, request, format=None):
        diaristas = Usuario.objects.filter(tipo_usuario=2)
        serializaer_diaristas_localidade = DiaristasLocalidadesSerializers(diaristas, many=True)
        return Response(serializaer_diaristas_localidade.data, status=status_http.HTTP_200_OK)
    
  