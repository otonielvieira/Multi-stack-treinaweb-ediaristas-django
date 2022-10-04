from django.urls import path


from api.views.diaristas_localidade_view import DiaristasLocalidades

urlpatterns = [
     path('diaristas/localidades', DiaristasLocalidades.as_view(), name='ediaristas-localidades-list'),
]



