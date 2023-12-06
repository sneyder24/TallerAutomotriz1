"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import principal,logout_user,principaliniciado
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', principal, name='start'),
    path('homepage/index.html', principal, name='start'),
    path('homepage/services.html/', views.services_view, name='services'),
    path('homepage/us.html/', views.us_view, name='us'),
    path('homepage/contactme.html/', views.contacme_view, name='contactme'),
    path('reiniciar',auth_views.LoginView.as_view(),name='login'),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reiniciar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logout/',logout_user,name="logout"),
    path('static/doc/Manualdeayudaclientes.pdf', views.Manualdeayudaclientes_view, name='Manualayudaclientes'),
    path('static/doc/Terminosycondiciones.pdf', views.TérminosyCondiciones_view, name='Terminos&Condiciones'),
    path('static/doc/Manualdeayudalogin.pdf', views.Manualdeayudalogin_view, name='Manualayudalogin'),

    path('admin/', admin.site.urls),
    path('login', principaliniciado, name="index" ),
    path('usuarios/', include('usuarios.urls') ),
    path('inventario/', include('inventario.urls')),
    path('mantenimiento/', include('mantenimiento.urls')),
    path('servicio/', include('servicio.urls')),
    path('facturacion/',include('facturacion.urls')),
    path('vehiculo/', include('vehiculo.urls')),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
