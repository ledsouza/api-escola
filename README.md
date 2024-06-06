## Django Escola API
![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)

API REST para gerenciamento de dados de uma escola fictícia, desenvolvida com Django REST Framework como parte do curso da Alura.

## Descrição

Este projeto implementa uma API completa para interagir com dados de uma escola. A API fornece acesso a informações sobre alunos, cursos e matrículas, e oferece diferentes níveis de permissão para diferentes tipos de usuários.

## Tecnologias Utilizadas

- Python 3
- Django
- Django REST Framework
- Django Cors Headers (para configurar CORS)

## Funcionalidades Detalhadas

**Versões da API:**

- **v1:** Versão inicial da API.
- **v2:** Inclui um campo adicional para o número de celular do aluno.

**Recursos:**

- **Alunos:** Consultar, adicionar, editar e remover informações de alunos.
- **Cursos:** Consultar, adicionar, editar e remover informações de cursos.
- **Matrículas:** Consultar, adicionar, editar e remover matrículas de alunos em cursos.

**Segurança:**

- **Autenticação:** A API requer autenticação para todas as requisições.
- **Autorização:** Diferentes tipos de usuários possuem permissões específicas para acessar e modificar dados.
- **Limite de Requisições:** Implementado um limite de requisições diárias por usuário para prevenir abusos.

**Funcionalidades Adicionais:**

- **CORS:** Configuração de CORS para permitir o consumo da API por um aplicativo React.

## Como Usar

1. Clone este repositório: `git clone https://github.com/seu_usuario/django-school-api.git`
2. Crie um ambiente virtual `poetry install`
3. Ative o ambiente virtual: `poetry shell`
4. Aplique as migrações: `python manage.py migrate`
5. Inicie o servidor de desenvolvimento: `python manage.py runserver`
6. Acesse a pasta do app React e instale as dependências: `npm install`
7. Atualize as dependências do npm com o seguinte comando: `npm update`
8. Inicie o servidor do frontend: `npm start`
