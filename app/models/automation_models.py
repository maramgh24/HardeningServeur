from pydantic import BaseModel


class AutomationRequest(BaseModel):
    configuration: str


class AutomationResponse(BaseModel):
    success: bool
    message: str
    playbook_file: str | None = None