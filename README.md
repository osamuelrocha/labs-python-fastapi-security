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

O projeto segue uma estrutura inspirada em boas práticas de organização:

```
app/
 ├── api/        → Rotas e dependências
 ├── core/       → Configurações e segurança
 ├── models/     → Schemas (Pydantic)
 ├── services/   → Regras de negócio
 └── main.py     → Entry point
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

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse:

* Swagger: http://localhost:8000/docs

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
