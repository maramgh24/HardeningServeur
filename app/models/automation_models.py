from pydantic import BaseModel
from typing import Literal



class AutomationRequest(BaseModel):
    configuration: str
    environment: Literal["test", "prod"]


class AutomationResponse(BaseModel):
    success: bool
    message: str
    playbook_file: str | None = None