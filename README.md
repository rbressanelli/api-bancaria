# 🏦 API Bancária Assíncrona com FastAPI

API RESTful assíncrona desenvolvida com **FastAPI** para gerenciamento de operações bancárias básicas, permitindo:

- cadastro de usuários
- autenticação com **JWT**
- criação de conta corrente
- realização de **depósitos**
- realização de **saques**
- consulta de **extrato bancário**

O projeto foi estruturado seguindo boas práticas de organização, com separação de rotas, uso de variáveis de ambiente, autenticação e documentação automática com OpenAPI.

Deploy na fastapi cloud no seguinte endereço:
<a href="https://api-bancaria-56dcb982.fastapicloud.dev/">API Bancária</a>

---

## 🚀 O que a aplicação faz

Esta aplicação simula uma API bancária simples, onde um usuário autenticado pode:

- se registrar na plataforma
- realizar login e obter um token JWT
- criar uma conta corrente
- efetuar depósitos
- efetuar saques, desde que haja saldo suficiente
- consultar o extrato da conta com as transações realizadas

---

## 🛠️ Principais tecnologias

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy Async**
- **SQLite**
- **Poetry**
- **Pydantic**
- **JWT**
- **Passlib**
- **Uvicorn**
- **python-dotenv**

---

## 📁 Estrutura do projeto

```bash
.
├── src
│   ├── api
│   │   └── routes
│   ├── core
│   ├── db
│   ├── models
│   ├── schemas
│   ├── services
│   └── main.py
├── .env
├── .env.example
├── .gitignore
├── poetry.lock
├── pyproject.toml
└── README.md
```

## ⚙️ Configuração do ambiente

### Clonar o projeto
git clone <url-do-repositorio>
cd nome-do-projeto

### Instalar as dependências com Poetry
poetry install

### Criar arquivo .env
cp .env.example .env <b>ou</b> copy .env.example .env

### executar
poetry run uvicorn src.main:app --reload

## 📚 Documentação automática
Após iniciar a aplicação, a documentação estará disponível em:

Swagger UI: http://127.0.0.1:8000/docs<br>
ReDoc: http://127.0.0.1:8000/redoc

## 🔐 Autenticação

A API utiliza autenticação com JWT.
Após realizar o login, utilize o token retornado no header das rotas protegidas:
Authorization: Bearer seu_token_aqui

# 📌 Endpoints


## 👤 Registro
POST /api/v1/auth/register

Realiza o cadastro de um novo usuário.

```
{
  "name": "Roberto",
  "email": "usuario@email.com",
  "password": "123456"
}
```

## 👤 Autenticação
POST /api/v1/auth/login

Autentica o usuário e retorna um token JWT.

```
{
  "email": "usuario@email.com",
  "password": "123456"
}
```
## 🏦 Conta corrente
POST /api/v1/accounts

Cria uma nova conta corrente para o usuário autenticado.

🔒 Requer autenticação

```
{
  "number": "1234567890",
  "initial_balance": 0
}
```
## 💸 Transações
POST /api/v1/accounts/{account_id}/transactions

Realiza uma transação bancária na conta informada.

🔒 Requer autenticação

➖ Saque

```
{
  "type": "withdraw",
  "amount": 50
}
```

➕ Depósito

```
{
  "type": "deposit",
  "amount": 100.50
}
```
## 📄 Extrato
GET /api/v1/accounts/{account_id}/statement

Retorna o extrato da conta com saldo atual e lista de transações.

🔒 Requer autenticação

# ✅ Regras e restrições

A aplicação possui validações para garantir a integridade das operações bancárias.

<b>Depósito</b><br>
- não é permitido realizar depósito com valor negativo<br>
- não é permitido realizar depósito com valor zero<br>

<b>Saque</b><br>
- não é permitido realizar saque com valor negativo<br>
- não é permitido realizar saque com valor zero<br>
- não é permitido sacar valor maior que o saldo disponível<br>


## 🔒 Observações sobre segurança
- as rotas de conta e transações são protegidas por JWT<br>
- o token deve ser enviado no header Authorization<br>
- senhas são armazenadas de forma criptografada<br>


# 📄 Variáveis de ambiente

Exemplo de .env.example:

APP_NAME=API Bancária
APP_VERSION=1.0.0
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=sqlite+aiosqlite:///./bank.db


# 🧹 .gitignore

O projeto inclui .gitignore para ambiente Python, evitando versionar arquivos temporários, cache, banco local, ambientes virtuais e arquivos sensíveis.


## 💡 Melhorias futuras
- paginação no extrato<br>
- atualização e exclusão de contas<br>
- uso de PostgreSQL<br>
- Alembic para versionamento do banco<br>
- Docker e Docker Compose<br>
- testes automatizados<br>
- refresh token<br>
- controle de permissões por usuário<br>

## 👨‍💻 Autor

Projeto desenvolvido como desafio técnico para prática de:

- FastAPI assíncrono<br>
- autenticação JWT<br>
- organização de APIs REST<br>
- modelagem de dados<br>
- validação de regras de negócio<br>
