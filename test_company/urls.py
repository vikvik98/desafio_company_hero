"""test_company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empresa.views import EmpresaViewSet
from funcionario.views import FuncionarioViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', FuncionarioViewSet.as_view({"get": "list", "post": "create"}), name="funcionarios/"),
    path('funcionarios/<int:funcionario_id>/',
         FuncionarioViewSet.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"}),
         name="funcionarios/funcionario_id/"),
    path('empresas/', EmpresaViewSet.as_view({"get": "list", "post": "create"}), name="empresas/"),
    path('empresas/<int:empresa_id>/',
         EmpresaViewSet.as_view({"get": "retrieve", "patch": "update", "delete": "destroy"}),
         name="empresas/empresa_id/"),
]
