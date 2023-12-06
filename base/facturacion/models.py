from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from mantenimiento.models import Cita
from usuarios.models import Usuario
import datetime


def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números.')
def alphabetic_validator(value):
    if not value.isalpha():
        raise ValidationError('El campo debe contener solo letras.')
class Venta(models.Model):
    fecha_venta= models.DateTimeField(verbose_name="Fecha de Venta", help_text="DD/MM/AAAA", default=datetime.date.today)
    fecha_cita=models.ForeignKey(Cita, on_delete=models.CASCADE, null=True, verbose_name=" Nombre Usuario",default=None)
    
    
    class formaPago(models.TextChoices):
        DEBITO='Debito',_("Tarjeta de Debito")
        CREDITO='Credito',_("Tarjeta de Credito")
        EFECTIVO='Efectivo',_("Efectivo")
    forma_pago= models.CharField(max_length=10, choices=formaPago.choices , verbose_name="Tipo de Pago")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=3,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
     
    class Meta:
        verbose_name_plural ="Ventas"

