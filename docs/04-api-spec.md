# 📡 API Specification

## 🔐 Auth

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

## 📩 FollowUp

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
