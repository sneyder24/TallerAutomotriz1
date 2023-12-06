from django.urls import path
from inventario.views import repuesto_listar, repuesto_crear, repuesto_modificar, repuesto_eliminar
from inventario.views import marcarepuesto_listar, marcarepuesto_crear, marcarepuesto_modificar, marcarepuesto_eliminar


urlpatterns = [
    path('repuestos/', repuesto_listar, name="repuestos" ),
    path('repuestos/crear/', repuesto_crear, name="repuestos-crear" ),
    path('repuestos/modificar/<int:pk>/', repuesto_modificar, name="repuestos-modificar" ),
    path('repuestos/eliminar/<int:pk>/', repuesto_eliminar, name="repuestos-eliminar" ),
    
    path('marcarepuesto/', marcarepuesto_listar, name="marcarepuestos" ),
    path('marcarepuesto/crear/', marcarepuesto_crear, name="marcarepuestos-crear" ),
    path('marcarepuesto/modificar/<int:pk>/', marcarepuesto_modificar, name="marcarepuestos-modificar" ),
    path('marcarepuesto/eliminar/<int:pk>/', marcarepuesto_eliminar, name="marcarepuestos-eliminar" ),
    
 
 
]