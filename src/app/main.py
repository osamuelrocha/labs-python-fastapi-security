from fastapi import FastAPI
from app.api.routes import auth
from app.api.routes import followup

app = FastAPI(title="FollowUp API")
app.include_router(auth.router)
app.include_router(followup.router)

@app.get("/")
def health_check():
    return {"status": "ok"}