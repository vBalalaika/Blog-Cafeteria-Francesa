from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Receta(models.Model):
    DIFICULTAD = (
        ('preparacion facil', 'Preparacion Facil'),
        ('preparacion intermedia', 'Preparacion Intermedia'),
        ('preparacion avanzada', 'Preparacion Avanzada'),
    )
    titulo = models.CharField(max_length=30)
    cantidad_de_personas = models.IntegerField()
    dificultad = models.CharField(max_length=40, choices = DIFICULTAD, default='preparacion facil', null=True, blank=True)
    imagenp = models.ImageField(upload_to='postres', null=True, blank=True)
    informacion_adicional = RichTextField()
    receta = models.FileField(upload_to='recetas', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Titulo: {self.titulo} | Dificultad: {self.dificultad} | Autor: {self.autor}'

    class Meta:
        verbose_name_plural = 'Recetas'