from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('sign/', views.sign, name='sign'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.edicionPerfil, name='edicionPerfil'),
    path('perfil/editar/cambiar_pass', views.CambiarPass.as_view(), name='cambio_password'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout')
]