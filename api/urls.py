from django.urls import path
from .views import endereco_cep_view, diaristas_localidade_view, disponibilidade_atendimento_cidade


urlpatterns = [
     path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(), name='ediaristas-localidades-list'),
     path('enderecos', endereco_cep_view.EnderecoCep.as_view(), name="endereco-cep-list"),
     path('diaristas/disponibilidade', disponibilidade_atendimento_cidade.DisponibilidadeAtendimentoCidade.as_view(),
     name='disponibilidade-atendimento-cidade-list')
     
]



