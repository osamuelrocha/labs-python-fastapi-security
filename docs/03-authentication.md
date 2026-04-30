# 🔐 Authentication

## 🔑 Estratégia

A API utiliza autenticação baseada em:

* Bearer Token
* JWT (JSON Web Token)

---

## 🔄 Fluxo de autenticação

1. Cliente envia credenciais
2. API valida usuário
3. API gera token JWT
4. Cliente usa token nos próximos requests

---

## 🧾 Estrutura do Token

Payload:

```json
{
  "sub": "username",
  "exp": "timestamp"
}
```

---

## 📌 Header obrigatório

```text
Authorization: Bearer {token}
```

---

## ⚠️ Regras

* Token expirado → acesso negado
* Token inválido → acesso negado
* Token ausente → acesso negado

---

## 🚧 Limitações atuais

* Usuário mockado
* Sem refresh token
* Sem blacklist

---

## 🔮 Evoluções futuras

* OAuth2 / OpenID Connect
* Integração com Identity Provider
* Rotação de chaves
