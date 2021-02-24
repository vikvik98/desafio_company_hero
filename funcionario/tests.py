from rest_framework.test import APITestCase
from rest_framework import status


class FuncionarioTestCase(APITestCase):

    def test_cadastro_sem_nome_completo(self):
        data = {
            "username": "tatakae",
            "password": "mikasa"
        }

        response = self.client.post('/funcionarios/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_sem_username(self):
        data = {
            "nome_completo": "Eren Jaeger",
            "password": "mikasa"
        }

        response = self.client.post('/funcionarios/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_sem_password(self):
        data = {
            "nome_completo": "Eren Jaeger",
            "username": "tatakae",
        }

        response = self.client.post('/funcionarios/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_correto(self):
        data = {
            "nome_completo": "Eren Jaeger",
            "username": "tatakae",
            "password": "mikasa"
        }

        response = self.client.post('/funcionarios/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_funcionarios(self):

        response = self.client.get('/funcionarios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_funcionarios_com_filtro(self):

        response = self.client.get('/funcionarios/?username=vikvik')
        self.assertEqual(response.status_code, status.HTTP_200_OK)