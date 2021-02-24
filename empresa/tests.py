from rest_framework.test import APITestCase
from rest_framework import status


class EmpresaTestCase(APITestCase):

    def test_cadastro_sem_razao_social(self):
        data = {
            "nome_fantasia": "empresa tatakae",
            "cnpj": "82.565.671/0001-64",
            "funcionarios": []
        }

        response = self.client.post('/empresas/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_sem_nome_fantasia(self):
        data = {
            "razao_social": "Empresa 3",
            "nome_fantasia": "empresa tatakae",
            "cnpj": "82.565.671/0001-64",
            "funcionarios": []
        }

        response = self.client.post('/empresas/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_sem_cnpj(self):
        data = {
            "razao_social": "Empresa 3",
            "nome_fantasia": "empresa tatakae",
            "funcionarios": []
        }

        response = self.client.post('/empresas/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
