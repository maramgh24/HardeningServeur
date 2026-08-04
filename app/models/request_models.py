from pydantic import BaseModel


class PlaybookRequest(BaseModel):

    requirement: str