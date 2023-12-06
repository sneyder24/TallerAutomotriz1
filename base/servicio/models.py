from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import datetime
from inventario.models import Repuesto
from usuarios.models import Usuario

def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números.')
def alphabetic_validator(value):
    if not all(char.isalpha() or char.isspace() for char in value):
            raise ValidationError('El campo debe contener solo letras y espacios.')

class Detalle_servicio(models.Model):
    nombreservicio= models.CharField(max_length=20,verbose_name="Nombre de Servicio",default="")
    tipo_servicio= models.CharField(max_length=45,verbose_name="Tipo de Servicio",default="")
    duracion = models.DurationField(verbose_name="Duración de la cita", default=datetime.timedelta(seconds=0))
    costoservicio = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Costo Servico",default=0.000)
    descripcion= models.CharField(max_length=45,verbose_name="Descripción",default="")
    def __str__(self):
        return f"{self.costoservicio}-{self.nombreservicio}"

    class Meta:
        verbose_name_plural = "Detalle_servicio"

class Servicio(models.Model):
    fecha_servicio=models.DateField(verbose_name="Fecha de Registro", help_text="MM/DD/AAAA", default=datetime.date.today)
    nombres= models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={'tipo_usuario': Usuario.TipoUsuario.MECANICO},verbose_name="Mecanico")
    kilometraje=models.CharField(max_length=6, verbose_name="Kilometraje", default=0,validators=[numeric_validator],blank=False)
    estado_vehiculo=models.CharField(max_length=45, verbose_name="Estado del vehiculo",default="",validators=[alphabetic_validator])
    observaciones=models.CharField(max_length=45, verbose_name="Observaciones",default="",validators=[alphabetic_validator])
    nombrerepuesto=models.ForeignKey(Repuesto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Costo Repuesto")
    nombreservicio=models.ForeignKey(Detalle_servicio,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Costo Servicio")
    def __str__(self):
        return f"({self.nombrerepuesto}){self.nombreservicio}"
    class Meta:
        verbose_name_plural = "Servicio"