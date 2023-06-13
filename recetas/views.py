from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from recetas.forms import BuscarRecetaForm
from recetas.models import Receta
from recetas.forms import RecetaForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')

def conocenos(request):
    foto = 'img/cafe.jpg'
    context = {'foto': foto}
    return render(request, 'conocenos.html', context=context)


def buscar_postre(request):
    search_to = request.GET.get('titulo', None)
    dific_to = request.GET.get('dificultad', None)

    if search_to:
        postres = Receta.objects.filter(titulo__icontains=search_to)
    else:
        postres = Receta.objects.all()

    if dific_to:
        postres = Receta.objects.filter(dificultad__icontains=dific_to)

    formulario_busqueda = BuscarRecetaForm()
    return render(request, 'buscar_postre.html', {'postres': postres, 'formulario': formulario_busqueda})


class UsuarioEsAutorMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        self.receta = get_object_or_404(Receta, pk=kwargs['pk'])
        if self.receta.autor != request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class ListaPostre(ListView):
    model = Receta
    template_name = 'lista_postre.html'
    context_object_name = 'recetas'

class CrearPostre(LoginRequiredMixin, CreateView):
    form_class = RecetaForm
    template_name = 'crear_postre.html'
    success_url = reverse_lazy('recetas:lista_postre')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.receta = self.request.FILES.get('recetas')
        return super().form_valid(form)

class DetallePostre(DetailView):
    model = Receta
    template_name = 'detalle_postre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecetaForm()
        return context

class EliminarPostre(UsuarioEsAutorMixin, DeleteView):
    model = Receta
    template_name = 'eliminar_postre.html'
    success_url = reverse_lazy('recetas:lista_postre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postre'] = self.object
        return context

class EditarPostre(UsuarioEsAutorMixin, UpdateView):
    model = Receta
    template_name = 'editar_postre.html'
    fields = ['titulo', 'cantidad_de_personas', 'dificultad',
              'imagenp', 'informacion_adicional', 'receta', 'autor']
    success_url = reverse_lazy('recetas:lista_postre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postre'] = self.object
        return context
