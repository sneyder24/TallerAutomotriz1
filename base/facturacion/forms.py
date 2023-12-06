from django import forms
from django.forms import ModelForm,widgets
from facturacion.models import Venta

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
        widgets={
            'fecha_venta': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
class VentaUpdateForm(ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"
        widgets={
            'fecha_venta': widgets.DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        }
