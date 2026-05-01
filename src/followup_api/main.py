from fastapi import FastAPI
from app.api.routes import followup

app = FastAPI(title="FollowUp Delivery API", version="1.0.0")
app.include_router(followup.router)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "followup"}
