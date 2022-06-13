from django import forms
from django.conf import settings
from .models import Veiculo, Motorista, Controle


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = '__all__'


class ControleForm(forms.ModelForm):
    class Meta:
        model = Controle
        fields = '__all__'
