from django import forms
from django.forms import ModelForm
from servicio.models import Servicio,Detalle_servicio

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
       
       
class ServicioUpdateForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
        
        
class Detalle_servicioForm(ModelForm):
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
    

class Detalle_servicioUpdateForm(ModelForm):
    
    class Meta:
        model = Detalle_servicio
        fields = "__all__"
 
  