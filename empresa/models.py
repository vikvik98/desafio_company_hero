from django.db import models

# Create your models here.
from funcionario.models import Funcionario


class Empresa(models.Model):
    razao_social = models.CharField("Razão social", max_length=100)
    nome_fantasia = models.CharField("Nome fantasia", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=20)
    funcionarios = models.ManyToManyField(Funcionario)

    class Meta:
        db_table = "empresa"
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
