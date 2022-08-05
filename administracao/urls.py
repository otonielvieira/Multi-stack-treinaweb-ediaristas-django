from django.urls import path
from .views import servico_views, usuario_views


urlpatterns = [
    path('servicos/cadastrar/', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar_servicos', servico_views.listar_servicos, name="listar_servicos"),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('usarios/cadastrar', usuario_views.cadastrar_usuario, name="cadatrar_usuario")

  
]
