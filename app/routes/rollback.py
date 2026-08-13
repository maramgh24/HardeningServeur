from fastapi import APIRouter

from app.services.rollback_service import rollback


router = APIRouter(
    prefix="/rollback",
    tags=["Rollback"]
)


@router.post("/execute")
def execute_rollback():

    return rollback()