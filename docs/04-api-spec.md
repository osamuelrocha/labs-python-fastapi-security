# 📡 API Specification

## 🔐 Auth API

Base URL: `http://localhost:8001`

### POST /auth/token

#### Request

```json
{
  "username": "admin",
  "password": "123456"
}
```

#### Response

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

---

## 📩 FollowUp API

Base URL: `http://localhost:8002`

### POST /followup/

#### Headers

```text
Authorization: Bearer {token}
```

#### Request

```json
{
  "message": "Cliente solicitou retorno",
  "customer_id": 123
}
```

#### Response

```json
{
  "status": "received",
  "user": {
    "sub": "admin"
  },
  "data": {
    "message": "...",
    "customer_id": 123
  }
}
```

---

## ❌ Possíveis erros

| Código | Descrição         |
| ------ | ----------------- |
| 401    | Token inválido    |
| 422    | Erro de validação |

### POST /followup/

#### Headers

```text
Authorization: Bearer {token}
```

#### Request

```json
{
  "message": "Cliente solicitou retorno",
  "customer_id": 123
}
```

#### Response

```json
{
  "status": "received",
  "user": {
    "sub": "admin"
  },
  "data": {
    "message": "...",
    "customer_id": 123
  }
}
```

---

## ❌ Possíveis erros

| Código | Descrição         |
| ------ | ----------------- |
| 401    | Token inválido    |
| 422    | Erro de validação |
