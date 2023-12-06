from django.db import models
from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

#validacion de numeros 
def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError('El campo debe contener solo números')
#validacion de letras y espacios 
def alphabetic_validator(value):
    if not all(char.isalpha() or char.isspace() for char in value):
            raise ValidationError('El campo debe contener solo letras y espacios')
#validacion de Contraseña
def validate_password(value):
    if len(value) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres")
    
    if not any(char.isdigit() for char in value):
        raise ValidationError("La contraseña debe contener al menos un número")
    
    if not any(char.isalpha() for char in value):
        raise ValidationError("La contraseña debe contener al menos una letra")
#validacion de Contraseña coincidan
def validate_passwords_match(value1, value2):
    if value1 != value2:
        raise ValidationError("Las contraseñas no coinciden")


#modulo arl
class Arl(models.Model):
    nombre_arl= models.CharField(max_length=20,verbose_name="Nombre Arl",blank=False,validators=[alphabetic_validator])
    telefono_arl= models.CharField(max_length=10,verbose_name="Telefono Arl",validators=[numeric_validator],blank=False)
    correo_arl= models.EmailField(max_length=50,verbose_name="Correo Arl",blank=False)
    fecha_inicioafi= models.DateField(verbose_name="Inicio De La Afiliación")
    fecha_vencimientoafi= models.DateField(verbose_name="Vencimiento De La Afiliación")
    def __str__(self):
        return self.nombre_arl
    class Meta:
        verbose_name_plural ="arls"    

#modulo usuario    
class Usuario(models.Model):
    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR = 'Administrador', _("Administrador")
        SECRETARIA = 'Secretaria', _("Secretaria")
        MECANICO = 'Mecanico', _("Mecanico")
    tipo_usuario = models.CharField(max_length=13, choices=TipoUsuario.choices, verbose_name="Tipo Usuario", default=TipoUsuario.MECANICO, blank=False)
    nombres = models.CharField(max_length=30, verbose_name="Nombres", default='', blank=False, validators=[alphabetic_validator])
    apellidos = models.CharField(max_length=30, verbose_name="Apellidos", default='', blank=False, validators=[alphabetic_validator])
    class TipoIdentificacion(models.TextChoices):
        CEDULA = 'Cédula Ciudadania', _("Cédula Ciudadania")
        TARJETA = 'Tarjeta Identidad', _("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA = 'Cédula Extrangería', _("Cédula de Extrangería")
    tipo_identificacion = models.CharField(max_length=18, choices=TipoIdentificacion.choices, verbose_name="Tipo de identificacion", default=TipoIdentificacion.CEDULA, blank=False)
    identificacion = models.CharField(max_length=10, verbose_name="Identificacion", default='', validators=[numeric_validator], unique=True, blank=False)
    telefono = models.CharField(max_length=11, verbose_name="Telefono", validators=[numeric_validator], blank=False)
    telefono2 = models.CharField(max_length=11, verbose_name="Segundo Telefono", validators=[numeric_validator], blank=True)
    nombreusuario = models.CharField(max_length=20, verbose_name="Nombre De Usuario", blank=False, default='')
    correo_personal = models.EmailField(max_length=50, verbose_name="Correo Personal", blank=False, default='')
    contrasena_validator = RegexValidator(regex=r'^[A-Za-z0-9]*$',message="La contraseña solo puede contener letras y números.",code='invalid_password')
    contraseña = models.CharField(max_length=10,verbose_name="Contraseña",blank=False,default='',validators=[validate_password, contrasena_validator])
    confirmarcontraseña = models.CharField(max_length=10, verbose_name="Confirmar Contraseña", blank=False, default='',validators=[validate_password, contrasena_validator])
    direccion = models.CharField(max_length=50, verbose_name="Dirección", blank=False)
    fecha_registro = models.DateField(verbose_name="Fecha de Registro", help_text="MM/DD/AAAA", auto_now_add=True,)
    class RH(models.TextChoices):
        OP = 'OP', _("O+")
        ON = 'ON', _("O-")
        AP = 'AP', _("A+")
        AN = 'AN', _("A-")
        BP = 'BP', _("B+")
        BN = 'BN', _("B-")
        ABP = 'ABP', _("AB+")
        ABN = 'ABN', _("AB-")
    rh = models.CharField(max_length=3, choices=RH.choices, verbose_name="Factor RH", blank=False)
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", blank=False)
    arl = models.ForeignKey(Arl, on_delete=models.SET_NULL, null=True, blank=False, verbose_name="ARL")
    
    
    #crear usuario en el sistema  y grupos
    def save(self, *args, **kwargs):
        super(Usuario, self).save(*args, **kwargs)
        user = User.objects.create_user(username=self.nombreusuario, password=self.contraseña)
        user.first_name = self.nombres
        user.last_name = self.apellidos
        user.email = self.correo_personal
        user.save()
        if self.tipo_usuario == Usuario.TipoUsuario.ADMINISTRADOR:
            grupo = Group.objects.get(name='Administrador')
        elif self.tipo_usuario == Usuario.TipoUsuario.SECRETARIA:
            grupo = Group.objects.get(name='Secretaria')
        elif self.tipo_usuario == Usuario.TipoUsuario.MECANICO:
            grupo = Group.objects.get(name='Mecanico')
        user.groups.add(grupo)
        
    def __str__(self):
        return f"({self.identificacion}) {self.nombres} {self.apellidos}"
    
    class Meta:
        verbose_name_plural = "usuarios"
         
#modulo Clientes
class Cliente(models.Model):
    nombres = models.CharField(max_length=30, verbose_name="Nombres", default='', blank=False, validators=[alphabetic_validator])
    apellidos = models.CharField(max_length=30, verbose_name="Apellidos", default='', blank=False, validators=[alphabetic_validator])
    class TipoIdentificacion(models.TextChoices):
        CEDULA = 'Cédula Ciudadania', _("Cédula Ciudadania")
        TARJETA = 'Tarjeta Identidad', _("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA = 'Cédula Extrangería', _("Cédula de Extrangería")
    tipo_identificacion = models.CharField(max_length=18, choices=TipoIdentificacion.choices, verbose_name="Tipo de identificacion", default=TipoIdentificacion.CEDULA, blank=False)
    identificacion = models.CharField(max_length=10, verbose_name="Identificacion", default='', validators=[numeric_validator], unique=True, blank=False)
    telefono = models.CharField(max_length=11, verbose_name="Telefono", validators=[numeric_validator], blank=False)
    telefono2 = models.CharField(max_length=11, verbose_name="Segundo Telefono", validators=[numeric_validator], blank=True)
    class Estado(models.TextChoices):
        ACTIVO = '1', _("Activo")
        INACTIVO = '0', _("Inactivo")
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", blank=False)

    class Meta:
        verbose_name_plural = "clientes"