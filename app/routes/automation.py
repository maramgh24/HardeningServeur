from fastapi import APIRouter

from app.models.automation_models import AutomationRequest
from app.services.automation_service import run_automation


router = APIRouter(
    prefix="/automation",
    tags=["Automation"]
)


@router.post("/run")
def automation(request: AutomationRequest):

    return run_automation(
        request.configuration,
        environment=request.environment
    )