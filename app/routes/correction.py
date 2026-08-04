from fastapi import APIRouter
from app.services.correction_service import correct_playbook

router = APIRouter()


@router.post("/correct")
def correct(request: dict):

    result = correct_playbook(
        request["playbook"],
        request["error"]
    )

    return {
        "corrected_playbook": result
    }