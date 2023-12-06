from django import forms

from django.forms import ModelForm 
from inventario.models import Marcarepuesto ,Repuesto


# formulario repuesto
class RepuestoForm(ModelForm):
    class Meta:
        model = Repuesto
        fields = "__all__"
        
class RepuestoUpdateForm(ModelForm):
    class Meta:
        model = Repuesto
        fields = "__all__"
     
     



# formulario marca repuesto
class MarcarepuestoForm(ModelForm):
    class Meta:
        model = Marcarepuesto
        fields = "__all__"
        exclude=["estado",]
        
class MarcarepuestoUpdateForm(ModelForm):
    class Meta:
        model = Marcarepuesto
        fields = "__all__"



 


 