from django.db import models
from django.contrib.auth.models import User


class InfAdicional(models.Model):
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Informacion adicional del usuario: {self.user}'

    class Meta:
        verbose_name_plural = 'Información Adicional'
