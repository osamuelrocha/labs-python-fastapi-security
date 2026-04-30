# 🏗️ Architecture

## 🧠 Visão Geral

A aplicação segue uma arquitetura modular inspirada em:

* Clean Architecture (simplificada)
* Separation of Concerns
* API-first design

---

## 📦 Camadas

### API Layer

Responsável por:

* Receber requisições HTTP
* Validar inputs
* Delegar para serviços

### Service Layer

Responsável por:

* Regras de negócio
* Autenticação

### Core Layer

Responsável por:

* Configurações
* Segurança (JWT)

### Models Layer

Responsável por:

* Schemas (Pydantic)

---

## 🔄 Fluxo

```text
Client → API → Service → Core → Response
```

---

## 🧱 Estrutura

```text
src/
 ├── api/
 ├── core/
 ├── models/
 ├── services/
 └── main.py
```

---

## ⚙️ Princípios aplicados

* Baixo acoplamento
* Alta coesão
* Separação de responsabilidades
* Facilidade de evolução
