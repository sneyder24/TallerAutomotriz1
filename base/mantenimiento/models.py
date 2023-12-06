from django.db import models
from vehiculo.models import Vehiculo
from servicio.models import Servicio
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

def alphabetic_validator(value):
    if not value.isalpha():
        raise ValidationError('El campo debe contener solo letras.')
        
class Cita(models.Model):
    placa=models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, verbose_name=" Nombre Usuario",default=None)
    fecha_cita= models.DateField(verbose_name="Fecha de cita",help_text="DD/MM/AAAA",blank=False)
    hora_cita= models.TimeField(max_length=15, verbose_name="Hora de cita", help_text="HH/MM/SS",blank=False)
    contacto = models.CharField(max_length=10,verbose_name="Contacto",default='',blank=False)    
    descripcion_cita= models.CharField(max_length=50,verbose_name="Descripcion de la cita",default='',blank=False,validators=[alphabetic_validator])
    nombreservicios= models.ForeignKey(Servicio,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Nombre servicio", default=None)

    class EstadoCita(models.TextChoices):
        Programada='Programada',_("Programada")
        Pospuesta='Pospuesta',_("Pospuesta")
        Cancelada='Cancelada',_("Cancelada")
        Enproceso='En proceso',_("Enproceso")
        Finalizada='Finalizada',_("Finalizada")
    estado_cita=models.CharField(max_length=10,choices=EstadoCita.choices,default=EstadoCita.Programada,verbose_name="Estado")
    def __str__(self):
        return f"({self.fecha_cita}){self.placa}{self.nombreservicios}"
     
    class Meta:
        verbose_name_plural = "Citas"