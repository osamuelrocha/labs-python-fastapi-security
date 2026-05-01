# 🐳 Docker Deployment

Este projeto está agora segregado em dois serviços distintos:

* `Auth API` rodando em `http://localhost:8001`
* `FollowUp API` rodando em `http://localhost:8002`

## 🛠️ Como rodar

No diretório raiz do repositório:

```bash
docker compose up --build
```

## 🔎 Endpoints disponíveis

Auth API:

* Health: `GET http://localhost:8001/`
* Swagger: `http://localhost:8001/docs`
* Token: `POST http://localhost:8001/auth/token`

FollowUp API:

* Health: `GET http://localhost:8002/`
* Swagger: `http://localhost:8002/docs`
* Receive FollowUp: `POST http://localhost:8002/followup/`

## 🔐 Fluxo da autenticação

1. Cliente solicita token ao Auth API.
2. Auth API retorna JWT.
3. Cliente envia token no header `Authorization: Bearer {token}` para o FollowUp API.

## 📦 Comandos úteis

```bash
docker compose up --build
```

```bash
docker compose down
```

## 💡 Observações

* `docker-compose.yml` constrói uma imagem base a partir do `Dockerfile`.
* Cada serviço expõe seu próprio FastAPI independente para autenticação e entrega de follow-up.
