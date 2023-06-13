from django.urls import path
from recetas import views

app_name = 'recetas'

urlpatterns = [
    path('', views.home, name='home'),
    path('conocenos/', views.conocenos, name='conocenos'),
    path('recetas/', views.ListaPostre.as_view(), name='lista_postre'),
    path('recetas/crear/', views.CrearPostre.as_view(), name='crear_postre'),
    path('recetas/buscar/', views.buscar_postre, name='buscar_postre'),
    path('recetas/<int:pk>/', views.DetallePostre.as_view(), name='detalle_postre'),
    path('recetas/<int:pk>/eliminar/', views.EliminarPostre.as_view(), name='eliminar_postre'),
    path('recetas/<int:pk>/editar/', views.EditarPostre.as_view(), name='editar_postre'),
]