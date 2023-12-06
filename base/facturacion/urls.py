from django.urls import path
from facturacion.views import venta_crear, venta_listar, venta_modificar, venta_eliminar
# Create your tests here.
urlpatterns = [
    path('venta/',venta_listar, name="ventas"),
    path('venta/crear/',venta_crear, name="ventas-crear"),
    path('venta/modificar/<int:pk>/',venta_modificar, name="ventas-modificar"),
    path('venta/eliminar/<int:pk>/',venta_eliminar, name="ventas-eliminar"),

]