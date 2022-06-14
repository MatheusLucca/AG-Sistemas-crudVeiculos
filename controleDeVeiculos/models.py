
from django.db import models
from datetime import datetime
# Create your models here.


class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    marca = models.CharField(max_length=100)
    veiculo = models.CharField(max_length=200)
    km_troca_oleo = models.FloatField(verbose_name='km Troca de óleo')

    def __str__(self):
        return self.veiculo


class Motorista(models.Model):
    cod_motorista = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    cnh = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Controle(models.Model):

    cod_veiculos = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cod_motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_saida = models.DateField()
    hora_saida = models.TimeField()
    km_saida = models.IntegerField()
    destino = models.CharField(max_length=200)
    data_retorno = models.DateField()
    hora_retorno = models.TimeField()
    km_retorno = models.IntegerField()
    km_percorrido = models.IntegerField()

    def __str__(self):
        str_data_saida = str(self.data_saida)
        data_saida = datetime.strptime(str_data_saida, '%Y-%m-%d').date()
        data_saida = datetime.strftime(data_saida, '%d/%m/%Y')
        str_data_retorno = str(self.data_retorno)
        data_retorno = datetime.strptime(str_data_retorno, '%Y-%m-%d').date()
        data_retorno = datetime.strftime(data_retorno, '%d/%m/%Y')

        title = 'Veículo: ' + self.cod_veiculos.veiculo + \
            ' - ' + 'Motorista: ' + self.cod_motorista.nome
        return title
