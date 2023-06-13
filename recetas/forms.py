from django import forms
from recetas.models import Receta

class BuscarRecetaForm(forms.Form):
    titulo = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dificultad = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'cantidad_de_personas', 'dificultad', 'imagenp', 'informacion_adicional', 'receta', 'autor']