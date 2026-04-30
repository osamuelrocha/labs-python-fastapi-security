from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="FollowUp API")
app.include_router(auth.router)

@app.get("/")
def health_check():
    return {"status": "ok"}