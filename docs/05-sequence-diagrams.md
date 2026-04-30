# 🔄 Sequence Diagrams

## 🔐 Autenticação

```text
Client → API: POST /auth/token
API → Service: validate user
Service → API: ok
API → Client: JWT Token
```

---

## 📩 Follow-up protegido

```text
Client → API: POST /followup (Bearer Token)
API → Security: validate token
Security → API: valid
API → Service: process request
API → Client: response
```
