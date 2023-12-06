from django import forms
from django.forms import ModelForm
from vehiculo.models import Vehiculo, Linea
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"
class VehiculoUpdateForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = "__all__"
class LineaForm(ModelForm):
    class Meta:
        model = Linea
        fields = "__all__"
class LineaUpdateForm(ModelForm):
    class Meta:
        model = Linea
        fields = "__all__"
