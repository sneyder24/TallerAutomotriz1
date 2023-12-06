from django.urls import path
from mantenimiento.views import cita_crear,cita_listar,cita_modificar,cita_eliminar

urlpatterns = [
 
    path('citas/', cita_listar, name="citas" ),
    path('citas/crear/', cita_crear, name="citas-crear" ),
    path('citas/modificar/<int:pk>/', cita_modificar, name="citas-modificar" ),
    path('citas/eliminar/<int:pk>/', cita_eliminar, name="citas-eliminar" ),

]