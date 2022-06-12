from django import forms
from .models import Veiculo, Motorista


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'
