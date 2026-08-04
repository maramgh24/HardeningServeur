from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ansible_service import check_ansible_playbook

router = APIRouter()


class ValidationRequest(BaseModel):
    playbook_path: str


@router.post("/validate-ansible")
def validate_ansible(request: ValidationRequest):
    return check_ansible_playbook(request.playbook_path)