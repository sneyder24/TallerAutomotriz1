from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números.')
def alphabetic_validator(value):
    if not value.isalpha():
        raise ValidationError('El campo debe contener solo letras.')
    
class Linea(models.Model):
    nombre_linea= models.CharField(max_length=20, verbose_name= "Linea",default='',blank=False,validators=[alphabetic_validator])
    class Cilindraje(models.TextChoices):
        MIL='1.000 cc',_("1.000 cc")
        MIL_CUATROCIENTOS='1.400 cc',_("1.400 cc")
        MIL_SEISCIENTOS='1.600 cc',_("1.600 cc")
        DOS_MIL='2.000 cc',_("2.000 cc")
    cilindraje=models.CharField(max_length=10,choices=Cilindraje.choices,verbose_name="Cilindraje")
    class Transmision(models.TextChoices):
        MANUAL='Manual',_("Manual")
        AUTOMATICA='Automatico',_("Automatico")
    transmision=models.CharField(max_length=10,choices=Transmision.choices,verbose_name="Transmision")
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=10,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    def __str__(self):
        return self.nombre_linea  
    class Meta:
        verbose_name_plural="linea"

class Vehiculo(models.Model):
    placa= models.CharField(max_length=6,verbose_name="Placa")
    class Marca(models.TextChoices):
        RENAULT='RENAULT',_("Renault")
        CHEVROLET='CHEVROLET',_("Chevrolet")
        HONDA='HONDA',_("Honda")
        CITROEN='CITROEN',_("Citroën")
        FORD='FORD',_("Ford")
        HYUNDAI='HYUNDAI',_("Hyundai")
        KIA='KIA',_("Kia")
        MAZDA='MAZDA',_("Mazda")
        MITSUBISHI='MITSUBISHI',_("Mitsubishi")
        NISSAN='NISSAN',_("Nissan")
    marca=models.CharField(max_length=10,choices=Marca.choices,verbose_name="Marca",blank=False)
    modelo= models.CharField(max_length=4, verbose_name="Modelo",default='',blank=False)
    tipo_aceite= models.CharField(max_length=25, verbose_name= "Tipo de Aceite")
    kilometraje= models.CharField(max_length=6, verbose_name= "Kilometraje",default='',validators=[numeric_validator],unique=True,blank=False)
    nombre_linea=models.ForeignKey(Linea, on_delete=models.CASCADE, null=True, verbose_name=" Nombre Linea",default=None)
    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=10,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")
    def __str__(self):
        return f"({self.placa}){self.identificacion}"
    class Meta:
        verbose_name_plural = "vehiculo"