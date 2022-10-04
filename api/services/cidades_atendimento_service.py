import requests
from rest_framework import serializers
import json


def buscar_cidade_cep(cep):
    requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json")
    
    if requisicao.status_code==400:
        raise serializers.ValidationError({"detail": "Erro ao buscar o CEP"})
    cidade_api = json.loads(requisicao.content)
    if 'erro' in cidade_api:
        raise serializers.ValidationError({"detail": "O CEP informado não foi encontrado"})
    return cidade_api
        