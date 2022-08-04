## Projeto sistema administrativo E-diaristas desenvolvido na imersão Multi-stack

### Instando o projeto

#### Clonar o projeto
`git clone https://github.com/otonielvieira/Multi-stack-treinaweb-ediaristas-django.git`

#### Instalar dependências
`pip install -r requirements.txt`

#### Alterar configurações do BD no arquivo `settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_do_bd',
        'USER': 'usuario_do_bb',
        'PASSWORD': 'senha_do_bd'
    }
}

```

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o servidor e testar o projeto
`python manage.py runserver`