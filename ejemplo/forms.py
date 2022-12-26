from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':'Escribir un Nombre'}))
    
class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'dni', 'fecha_nac', 'direccion']