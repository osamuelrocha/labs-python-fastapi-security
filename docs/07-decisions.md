# 📑 Architecture Decisions

## 🧠 ADR-001: Uso de FastAPI

### Decisão

Utilizar FastAPI como framework principal.

### Motivo

* Alta performance
* Tipagem com Pydantic
* Documentação automática

---

## 🔐 ADR-002: Uso de JWT

### Decisão

Autenticação via JWT.

### Motivo

* Stateless
* Simples para laboratório
* Fácil integração futura

---

## 🧩 ADR-003: Estrutura modular

### Decisão

Separar em camadas (api, services, core).

### Motivo

* Escalabilidade
* Manutenção
* Clareza arquitetural
