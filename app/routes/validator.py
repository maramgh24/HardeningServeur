from fastapi import APIRouter

from app.services.validator_service import validate_yaml


router = APIRouter(
    prefix="/validator",
    tags=["Validator"]
)


@router.post("/validate")
def validate(request: dict):

    playbook = request["playbook"]

    return validate_yaml(playbook)