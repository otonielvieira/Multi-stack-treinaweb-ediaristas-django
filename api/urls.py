from django.urls import path

from api.views.diaristas_localidade_view import DiasristasLocalidades

urlpatterns = [
     path('diaristas/localidades', DiasristasLocalidades.as_view(), name='ediaristas-localidades-list'),
]



