from fastapi import APIRouter, HTTPException
from app.models.schemas import TokenRequest, TokenResponse
from app.services.auth_service import authenticate_user, generate_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/token", response_model=TokenResponse)
def login(data: TokenRequest):
    user = authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = generate_token(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }