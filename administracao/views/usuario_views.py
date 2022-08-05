from django.shortcuts import render

from administracao.forms.usuario_forms import UsuarioForm


def cadastrar_usuario(request):
    if request.method == "POST":
         form_usuario = UsuarioForm(request.POST)
         if  form_usuario.is_valid():
              form_usuario.save()
    else:
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})


