from django.urls import path
from usuarios.views import usuario_listar, usuario_crear, usuario_modificar, usuario_eliminar
from usuarios.views import arl_listar, arl_crear, arl_modificar, arl_eliminar
from usuarios.views import cliente_listar, cliente_crear, cliente_modificar, cliente_eliminar

urlpatterns = [
    path('usuarios/', usuario_listar, name="usuarios" ),
    path('usuarios/crear/', usuario_crear, name="usuarios-crear" ),
    path('usuarios/modificar/<int:pk>/', usuario_modificar, name="usuarios-modificar" ),
    path('usuarios/eliminar/<int:pk>/', usuario_eliminar, name="usuarios-eliminar"),
    
    path('arl/', arl_listar, name="arls" ),
    path('arl/crear/', arl_crear, name="arls-crear" ),
    path('arl/modificar/<int:pk>/', arl_modificar, name="arls-modificar" ),
    path('arl/eliminar/<int:pk>/', arl_eliminar, name="arls-eliminar" ),
    
    path('cliente/', cliente_listar, name="clientes" ),
    path('cliente/crear/', cliente_crear, name="clientes-crear" ),
    path('cliente/modificar/<int:pk>/', cliente_modificar, name="clientes-modificar" ),
    path('cliente/eliminar/<int:pk>/', cliente_eliminar, name="clientes-eliminar" ),
 
 
]