from django.db import transaction
from rest_framework import serializers
from empresa.models import Empresa
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioListSerializer


class FuncionarioEmpresaListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Funcionario
        fields = (
            'id',
            'username',
            'nome_completo'
        )

    def get_username(self, obj):
        return obj.usuario_django.username


class EmpresaListSerializer(serializers.ModelSerializer):
    funcionarios = FuncionarioEmpresaListSerializer(many=True)

    class Meta:
        model = Empresa
        fields = (
            'id',
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'funcionarios'
        )

class EmpresaCreateSerializer(serializers.ModelSerializer):
    funcionarios = serializers.ListField(write_only=True)

    def validate(self, data):

        if Empresa.objects.filter(razao_social=data.get("razao_social")).exists():
            raise serializers.ValidationError({"razao_social": "Já existe uma empresa com essa razão social."})

        if Empresa.objects.filter(nome_fantasia=data.get("nome_fantasia")).exists():
            raise serializers.ValidationError({"nome_fantasia": "Já existe uma empresa com essa nome fantasia."})

        if Empresa.objects.filter(cnpj=data.get("cnpj")).exists():
            raise serializers.ValidationError({"cnpj": "Já existe uma empresa com esse cnpj."})

        if data.get("funcionarios"):
            for funcionario in data.get("funcionarios"):
                try:
                    Funcionario.objects.get(id=funcionario)
                except:
                    raise serializers.ValidationError(
                        {'funcionarios': 'Algum dos funcionarios informados não existe em nossa base de dados.'})

        return data

    class Meta:
        model = Empresa
        fields = (
            'id',
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'funcionarios'
        )

    @transaction.atomic
    def create(self, validated_data):
        empresa = Empresa(
            razao_social=validated_data['razao_social'],
            nome_fantasia=validated_data['nome_fantasia'],
            cnpj=validated_data['cnpj']
        )
        empresa.save()
        if validated_data['funcionarios']:
            for id in validated_data['funcionarios']:
                empresa.funcionarios.add(id)

        return empresa


class EmpresaUpdateSerializer(serializers.ModelSerializer):
    funcionarios = serializers.ListField()

    def validate(self, data):

        if data.get("funcionarios", None):
            for funcionario in data.get("funcionarios"):
                try:
                    Funcionario.objects.get(id=funcionario)
                except:
                    raise serializers.ValidationError(
                        {'funcionarios': 'Algum dos funcionarios informados não existe em nossa base de dados.'})

        return data

    class Meta:
        model = Empresa
        fields = (
            'id',
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'funcionarios'
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.razao_social = validated_data["razao_social"]
        instance.nome_fantasia = validated_data["nome_fantasia"]
        instance.cnpj = validated_data["cnpj"]
        instance.funcionarios.clear()

        if validated_data["funcionarios"]:
            for id in validated_data["funcionarios"]:
                funcionario = Funcionario.objects.get(id=id)
                instance.funcionarios.add(funcionario)

        instance.save()

        return validated_data