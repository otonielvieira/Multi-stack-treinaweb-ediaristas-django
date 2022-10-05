from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField
import os
from django.core.validators import validate_image_file_extension


#metodo para guardar o caminho das fotos
def nome_arquivo_foto(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.join('usuarios', filename)

def nome_arquivo_documento(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    
    return os.join('documentos', filename)
    
    
class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
    (1, "Cliente"),
    (2, "Diarista")
);
    nome_completo = models.CharField(max_length=255, null=True, blank=False)
    cpf = BRCPFField(null=True, unique=True, blank=False)
    nascimento = models.DateField(null=True, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    telefone = models.EmailField(null=True, blank=False)
    tipo_usuario = models.IntegerField(choices=TIPO_USUARIO_CHOICES, null=True, blank=False)
    reputacao = models.FloatField(null=False, blank=False, default=5)
    chave_pix = models.CharField(null=True, blank=True, max_length=255)
    foto_documento = models.ImageField(null=True, upload_to=nome_arquivo_foto, validators=[validate_image_file_extension,])
    foto_usuario = models.ImageField(null=True, upload_to=nome_arquivo_documento, validators=[validate_image_file_extension,])
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome_completo', 'cpf', 'telefone', 'tipo_usuario', 'reputacao', 
                       'chave_pix', 'foto_documento', 'foto_usuario')
    
#tabela de relacionamento que salva as cidades e relaciona aos usuarios 
class CidadesAtendimento(models.Model):
    codigo_ibge = models.IntegerField(null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, related_name='cidades_atendidas')
     
