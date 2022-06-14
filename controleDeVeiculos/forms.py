from django import forms
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

    data_saida = forms.DateField(
        label='Data Saida',
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y',
                       '%d-%m-%Y',
                       '%Y-%m-%d',      # '2006-10-25'
                       '%m/%d/%Y',       # '10/25/2006'
                       '%m/%d/%y'],    # '10/25/06',
    )
    data_retorno = forms.DateField(
        label='Data Retorno',
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y',
                       '%d-%m-%Y',
                       '%Y-%m-%d',      # '2006-10-25'
                       '%m/%d/%Y',       # '10/25/2006'
                       '%m/%d/%y'],
    )

    class Meta:

        model = Controle
        fields = '__all__'
