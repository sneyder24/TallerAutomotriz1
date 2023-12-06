from django.urls import path
from servicio.views import servicio_listar, servicio_crear, servicio_modificar, servicio_eliminar
from servicio.views import detalleservicio_listar, detalleservicio_crear, detalleservicio_modificar, detalleservicio_eliminar
 

urlpatterns = [
    path('servicio/', servicio_listar, name="servicios" ),
    path('servicio/crear/', servicio_crear, name="servicios-crear" ),
    path('servicio/modificar/<int:pk>/', servicio_modificar, name="servicios-modificar" ),
    path('servicio/eliminar/<int:pk>/', servicio_eliminar, name="servicios-eliminar" ),
    
    path('detalle_servicio/', detalleservicio_listar, name="detalleservicios" ),
    path('detalle_servicio/crear/', detalleservicio_crear, name="detalleservicios-crear" ),
    path('detalle_servicio/modificar/<int:pk>/', detalleservicio_modificar, name="detalleservicios-modificar" ),
    path('detalle_servicio/eliminar/<int:pk>/', detalleservicio_eliminar, name="detalleservicios-eliminar" ),
    
     

]