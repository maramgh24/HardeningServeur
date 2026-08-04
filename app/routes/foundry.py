from fastapi import APIRouter
from app.services.foundry_service import generate_response


router = APIRouter()


@router.post("/test-foundry")
def test_foundry():

    result = generate_response(
        "Explique ce qu'est Ansible en deux phrases"
    )

    return result