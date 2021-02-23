from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from empresa.models import Empresa
from empresa.serializers import EmpresaListSerializer, EmpresaCreateSerializer, EmpresaUpdateSerializer

# Create your views here.



class EmpresaViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            raise Http404

    def list(self, request):
        instances = Empresa.objects.all()

        serializer = EmpresaListSerializer(instances, many=True)
        return Response(serializer.data)

    def retrieve(self, request, empresa_id):
        instance = self.get_object(empresa_id)
        serializer = EmpresaListSerializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmpresaCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, empresa_id):
        instance = self.get_object(empresa_id)
        serializer = EmpresaUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, empresa_id):
        instance = self.get_object(empresa_id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
