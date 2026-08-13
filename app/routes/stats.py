from fastapi import APIRouter

from app.services.stats_service import stats_service


router = APIRouter(
    prefix="/stats",
    tags=["Statistics"]
)


@router.get("")
def get_statistics():

    return stats_service.get_stats()