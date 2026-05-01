from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="FollowUp Auth API", version="1.0.0")
app.include_router(auth.router)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "auth"}
