from fastapi import APIRouter

from app.models.request_models import PlaybookRequest
from app.services.foundry_service import generate_ansible_playbook

from datetime import datetime
from pathlib import Path


router = APIRouter()


@router.post("/generate-playbook")
def generate_playbook(
        request: PlaybookRequest
):

    playbook = generate_ansible_playbook(
        request.requirement
    )


    filename = (
        f"playbook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yml"
    )


    path = Path(
        "generated_playbooks"
    ) / filename


    path.write_text(
        playbook,
        encoding="utf-8"
    )


    return {
        "message": "Playbook generated successfully",
        "file": str(path),
        "content": playbook
    }