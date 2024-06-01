from fastapi import APIRouter
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.controllers.addition_controller import handle_addition

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request: AdditionRequest):
    return handle_addition(request)
