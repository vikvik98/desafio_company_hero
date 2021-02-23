from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from funcionario.models import Funcionario
from empresa.models import Empresa


class EmpresaFuncionarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = (
            'id',
            'razao_social',
            'nome_fantasia',
            'cnpj',
        )

class FuncionarioListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    empresas = serializers.SerializerMethodField()

    class Meta:
        model = Funcionario
        fields = (
            'id',
            'username',
            'nome_completo',
            'empresas'
        )

    def get_username(self, obj):
        return obj.usuario_django.username

    def get_empresas(self, obj):
        return EmpresaFuncionarioListSerializer(obj.empresa_set.all(), many=True).data


class FuncionarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    def validate(self, data):

        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({"username": "Username já cadastrado no banco de dados."})

        return data

    class Meta:
        model = Funcionario
        fields = (
            'id',
            'username',
            'password',
            'nome_completo'
        )

    @transaction.atomic
    def create(self, validated_data):
        user = User(
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()

        funcionario = Funcionario(
            usuario_django=user,
            nome_completo=validated_data['nome_completo']
        )
        funcionario.save()
        return funcionario


class FuncionarioUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({"username": "Username já cadastrado no banco de dados."})

        return data

    class Meta:
        model = Funcionario
        fields = (
            'id',
            'username',
            'password',
            'nome_completo'
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.usuario_django.username = validated_data["username"]
        instance.usuario_django.set_password(validated_data["password"])
        instance.usuario_django.save()
        instance.nome_completo = validated_data["nome_completo"]
        instance.save()

        return validated_data
