from django.urls import path
from vehiculo.views import vehiculo_crear, vehiculo_listar, vehiculo_modificar, vehiculo_eliminar
from vehiculo.views import linea_crear, linea_listar, linea_modificar, linea_eliminar

# Create your tests here.
urlpatterns = [
    path('vehiculo/', vehiculo_listar, name='vehiculos'),
    path('vehiculo/crear/', vehiculo_crear, name='vehiculos-crear'),
    path('vehiculo/modificar/<int:pk>/', vehiculo_modificar, name='vehiculos-modificar'),
    path('vehiculo/eliminar/<int:pk>/', vehiculo_eliminar, name='vehiculos-eliminar'),

    path('linea/', linea_listar, name='lineas'),
    path('linea/crear/', linea_crear, name='lineas-crear'),
    path('linea/modificar/<int:pk>/', linea_modificar, name='lineas-modificar'),
    path('linea/eliminar/<int:pk>/', linea_eliminar, name='lineas-eliminar'),
]
