from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Funcionario(models.Model):
    usuario_django = models.OneToOneField(User, related_name="funcionario", on_delete=models.CASCADE, unique=True)
    nome_completo = models.CharField("Nome completo", max_length=180)

    class Meta:
        db_table = "funcionario"
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'