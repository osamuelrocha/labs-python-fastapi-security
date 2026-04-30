from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps import get_current_user

router = APIRouter(prefix="/followup", tags=["FollowUp"])


class FollowUpRequest(BaseModel):
    message: str
    customer_id: int


@router.post("/")
def receive_followup(
    data: FollowUpRequest,
    user=Depends(get_current_user)
):
    return {
        "status": "received",
        "user": user,
        "data": data
    }