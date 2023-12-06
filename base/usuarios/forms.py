from django import forms
from django.utils import timezone
from django.forms import ModelForm,widgets
from usuarios.models import Usuario, Arl,Cliente

# Formulario Usuario
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["estado",]
        widgets={
            'fecha_registro': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
        
# Formulario Usuario Modificar      
class UsuarioUpdateForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        exclude=["documento","rh","fecha_registro"]
        
# Formulario Arl      
class ArlForm(ModelForm):
    class Meta:
        model = Arl
        fields = "__all__"
        exclude = ["estado"]
        widgets = {
            'fecha_inicioafi': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'fecha_vencimientoafi': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
        }

# Formulario  Modificar Arl  
class ArlUpdateForm(ModelForm):
    class Meta:
        model = Arl
        fields = "__all__"
        exclude = ["fecha_inicioafi"]
        widgets = {
            'fecha_inicioafi': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
            'fecha_vencimientoafi': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().strftime('%Y-%m-%d')}),
        }
       
# Formulario cliente Modificar  
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        exclude=["estado",]
        widgets={
            'fecha_registro': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
        
# Formulario cliente Modificar      
class ClienteUpdateForm(ModelForm):
    class Meta:
        model =Cliente
        fields = "__all__"
        exclude=["documento","fecha_registro"]  
    