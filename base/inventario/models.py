from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def alphabetic_validator(value):
    if not all(char.isalpha() or char.isspace() for char in value):
            raise ValidationError('El campo debe contener solo letras y espacios.')
class Marcarepuesto(models.Model):
    nombremarcarepuesto= models.CharField(max_length=25,verbose_name="Nombre Marca Repuesto",validators=[alphabetic_validator],blank=False)
    class GamaRepuesto(models.TextChoices):
        Baja='Baja',_("Baja")
        Alta='Alta',_("Alta")
    gama_repuesto=models.CharField(max_length=4,choices=GamaRepuesto.choices,default=GamaRepuesto.Alta,verbose_name="Gama Repuesto",blank=False)
    def __str__(self):
        return self.nombremarcarepuesto
    class Meta:
            verbose_name_plural ="marcarepuesto" 
class Repuesto(models.Model):
    nombrerepuesto= models.CharField(max_length=30,verbose_name="Nombre Repuesto",validators=[alphabetic_validator],blank=False)
    costorepuesto = models.DecimalField(max_digits=10,decimal_places=3,verbose_name="Costo Repuesto",default=0.00,blank=False)    
    stock = models.IntegerField(verbose_name="Cantidad Inventario",default=0,blank=False ) 
    marcarepuesto = models.ForeignKey(Marcarepuesto, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Marca Repuesto")
    class TipoRepuesto(models.TextChoices):
        Insumo='Insumo',_("Insumo")
        Repuesto='Repuesto',_("Repuesto")
    tipo_repuesto=models.CharField(max_length=8,choices=TipoRepuesto.choices,default=TipoRepuesto.Repuesto,verbose_name="Repuesto",blank=False)
    descripcionrepuesto=models.CharField(max_length=85,verbose_name="Descripcion Repuesto",validators=[alphabetic_validator],blank=True)
    def __str__(self):
        return f"${self.costorepuesto}-{self.nombrerepuesto}"
    
    class Meta:
        verbose_name_plural ="repuesto" 

 
