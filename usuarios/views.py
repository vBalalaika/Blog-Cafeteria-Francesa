from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import InfAdicional
from usuarios.forms import EditarPerfil, RegistroFormulario

def sign(request):

    if request.method == 'POST':

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            login(request, user)

            InfAdicional.objects.get_or_create(user=request.user)

            return redirect('recetas:home')
        else:
            return render(request, 'sign.html', {'form': formulario})

    formulario = AuthenticationForm()
    return render(request, 'sign.html', {'form': formulario})


def registro(request):

    if request.method == 'POST':

        formulario = RegistroFormulario(request.POST)

        if formulario.is_valid():
            formulario.save()

            return redirect('usuarios:sign')
        else:
            return render(request, 'registro.html', {'form': formulario})

    formulario = RegistroFormulario()
    return render(request, 'registro.html', {'form': formulario})


@login_required
def perfil(request):

    usuario = request.user
    info_adicional = InfAdicional.objects.get_or_create(user=request.user)

    contexto = {'usuario': usuario,'info_adicional': info_adicional}

    return render(request, 'perfil.html', contexto)


@login_required
def edicionPerfil(request):
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                infadicional = request.user.infadicional
                infadicional.avatar = formulario.cleaned_data.get('avatar')
                infadicional.save()
            formulario.save()
            return redirect('usuarios:perfil')
        else:
            return render(request, 'edicionPerfil.html', {'form': formulario})
    formulario = EditarPerfil(initial={'avatar': request.user.infadicional.avatar}, instance=request.user)
    return render(request, 'edicionPerfil.html', {'form': formulario})


class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambio_password.html'
    success_url = reverse_lazy('usuarios:edicionPerfil')
