from fastapi import APIRouter
from pydantic import BaseModel

from app.services.validator_service import validate_yaml


router = APIRouter()


class PlaybookValidationRequest(BaseModel):
    playbook: str


@router.post("/validate-playbook")
def validate_playbook(request: PlaybookValidationRequest):

    result = validate_yaml(request.playbook)

    return result