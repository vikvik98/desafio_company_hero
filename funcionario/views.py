from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioListSerializer, FuncionarioCreateSerializer, FuncionarioUpdateSerializer


# Create your views here.
class FuncionarioViewSet(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            return Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            raise Http404

    def list(self, request):
        instances = Funcionario.objects.all()

        if request.GET.get("username", None):
            instances = instances.filter(usuario_django__username=request.GET.get("username").lower())

        serializer = FuncionarioListSerializer(instances, many=True)
        return Response(serializer.data)

    def retrieve(self, request, funcionario_id):
        instance = self.get_object(funcionario_id)
        serializer = FuncionarioListSerializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = FuncionarioCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, funcionario_id):
        instance = self.get_object(funcionario_id)
        serializer = FuncionarioUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, funcionario_id):
        instance = self.get_object(funcionario_id)
        instance.usuario_django.delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)