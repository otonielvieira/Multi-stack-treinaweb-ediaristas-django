from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from administracao.models import Servico as ServicoMOdel
from ..serializers import servico_serializer


class Servico(APIView):
    def get(self, request, format=None):
        servicos = ServicoMOdel.objects.order_by('posicao')
        serializer_servico = servico_serializer.ServicoSerializer(servicos, many=True)
        return Response(serializer_servico.data, status=status_http.HTTP_200_OK)