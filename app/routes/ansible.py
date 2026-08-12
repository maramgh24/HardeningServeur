from fastapi import APIRouter

from app.services.ansible_service import execute_playbook


router = APIRouter(
    prefix="/ansible",
    tags=["Ansible"]
)


@router.post("/execute")
def execute(request: dict):

    playbook_path = request["playbook_path"]

    return execute_playbook(
        playbook_path
    )