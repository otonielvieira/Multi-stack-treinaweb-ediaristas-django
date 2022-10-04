from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadesSerializers
from rest_framework import status as status_http
from ..services import cidades_atendimento_service




class DiaristasLocalidades(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        cidade = cidades_atendimento_service.buscar_cidade_cep(cep)
        print(cidade)
        diaristas = Usuario.objects.filter(tipo_usuario=2)
        serializaer_diaristas_localidade = DiaristasLocalidadesSerializers(diaristas, many=True)
        return Response(serializaer_diaristas_localidade.data, status=status_http.HTTP_200_OK)
    
  