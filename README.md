# 🚀 FastAPI FollowUp API (Lab)

API de laboratório desenvolvida com **FastAPI**, implementando autenticação via **Bearer Token (JWT)** e um endpoint protegido simulando o recebimento de follow-ups.

---

## 🧠 Objetivo

Este projeto tem como objetivo demonstrar:

* Estrutura organizada de API em FastAPI
* Autenticação baseada em JWT
* Proteção de endpoints com Bearer Token
* Separação de responsabilidades (routes, services, core)

---

## 🧱 Arquitetura

O projeto está agora segmentado em dois serviços independentes:

* `Auth API` — responsável pela emissão de JWT
* `FollowUp API` — responsável por receber follow-ups autorizados

A estrutura do repositório fica assim:

```
src/
 ├── auth_api/          → Serviço FastAPI de autenticação
 ├── followup_api/      → Serviço FastAPI de follow-up
 └── app/               → Código compartilhado (routes, core, models, services)
```

---

## 🔐 Autenticação

A autenticação é feita via JWT.

### Gerar Token

POST `/auth/token`

```json
{
  "username": "admin",
  "password": "123456"
}
```

---

## 🔒 Endpoint Protegido

POST `/followup/`

Header:

```
Authorization: Bearer {token}
```

Body:

```json
{
  "message": "Cliente solicitou retorno",
  "customer_id": 123
}
```

---

## ▶️ Executando o projeto

### Localmente

```bash
cd src
pip install -r requirements.txt
uvicorn auth_api.main:app --reload --host 0.0.0.0 --port 8001
uvicorn followup_api.main:app --reload --host 0.0.0.0 --port 8002
```

### Com Docker

```bash
docker compose up --build
```

Acesse:

* Auth API Swagger: http://localhost:8001/docs
* FollowUp API Swagger: http://localhost:8002/docs

---

## 🧪 Observações

* Projeto com autenticação mock (usuário fixo)
* Ideal para laboratório e evolução futura
* Pode ser expandido com:

  * Banco de dados
  * Refresh token
  * RBAC / autorização por roles
  * Logs estruturados
  * Observabilidade

---

## 📌 Roadmap

* [ ] Integração com banco (PostgreSQL)
* [ ] Hash de senha (bcrypt)
* [ ] Deploy em cloud (Azure / AWS)
* [ ] Pipeline CI/CD

---

## 👨‍💻 Autor

Samuel Rocha
