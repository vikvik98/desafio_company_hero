# Desafio Company Hero

## Explicação geral sobre o projeto

* O projeto foi dividido em 3 modulos: test_company(onde fica os arquivos gerais), modulo de funcionario e modulo de empresa;
* As regras de negocio e validações ficaram no arquivo serializers.py de seus respectivos modulos;
* Os testes unitarios ficaram no arquivo tests.py de seus respectivos modulos.

## Testes Unitarios

* O foco dos testes unitarios usados nesse projeto foi testar o status code dos endpoints para saber se está tudo ok com os status code fornecido pelos endpoints;
* Para rodar os testes basta clonar o projeto executando o comando "git clone https://github.com/vikvik98/desafio_company_hero.git";
* Criar uma virtual env da forma que achar mais confortavel;
* Instalar os requirements com o comando "pip install -r requirements.txt";
* E por fim rodar o comando "python manage.py test".

## Endpoints e Json exemplos

* Como a API está hospedada em um servidor heroku, para testar os endpoints não vai ser necessario está rodando o projeto localmente;

* https://teste-company-hero.herokuapp.com/funcionarios/ Endpoint pronto para receber um metodo GET e Post na qual é responsavel de retornar os funcionarios e criá-los tambem, Exemplo de json para criação de funcionario: {
   "nome_completo": "Eren Jaeger",
    "username": "tatakae",
    "password": "mikasa"
}

* Lembrando que pelo mesmo endpoint acima é possivel fazer uma filtragem de funcionarios pelo seu username(No projeto essa filtragem é feita de forma flexivel, ou seja, não é preciso digitar o username completo para filtrar, por exemplo, se eu digitar "https://teste-company-hero.herokuapp.com/funcionarios/?username=tata" irá retornar o funcionario Eren Jaeger)

* O endpoint tambem foi projetado para trazer um funcionario pelo seu id, como por exemplo: https://teste-company-hero.herokuapp.com/funcionarios/funcionario_id/" dessa forma é possivel Visualizar com o metodo GET, Editar com o metodo PATCH, e Deletar com o metodo DELETE

* Com o Endpoint https://teste-company-hero.herokuapp.com/empresas/ é possivel trazer as empresas com o metodo GET ou criar com o metodo POST, na criação de empresa foi projetado para receber a associação de varios funcionarios ou nenhum, um exemplo de json para criação de empresa: 
{
	"razao_social": "Empresa 3",
    "nome_fantasia": "empresa 3",
    "cnpj": "82.565.671/0001-64",
    "funcionarios": [1, 2]
} ;

* Com o Endpoint https://teste-company-hero.herokuapp.com/empresas/empresa_id/ é possivel trazer uma empresa especifica com o metodo GET, editar com o metodo PATCH ou deletar com o metodo DELETE.

## Contatos para qualquer duvida que houver sobre o projeto
* Email: vinicius.c.mascarenhas@hotmail.com
* Linkedin: https://www.linkedin.com/in/vinicius-tomaz-4b07358b/
* Whatsapp: (86)98891-0894
