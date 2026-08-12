from fastapi import APIRouter
from pathlib import Path
from datetime import datetime

from app.models.request_models import PlaybookRequest
from app.services.foundry_service import generate_ansible_playbook


router = APIRouter(
    prefix="/foundry",
    tags=["Foundry"]
)


@router.post("/generate-playbook")
def generate_playbook(request: PlaybookRequest):

    playbook = generate_ansible_playbook(
        request.requirement
    )

    filename = (
        f"playbook_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.yml"
    )

    directory = Path("generated_playbooks")
    directory.mkdir(exist_ok=True)

    path = directory / filename

    path.write_text(
        playbook,
        encoding="utf-8"
    )

    return {
        "message": "Playbook generated successfully",
        "file": str(path),
        "content": playbook
    }