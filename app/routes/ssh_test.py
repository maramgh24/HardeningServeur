from fastapi import APIRouter
from app.services.ssh_service import execute_command

router = APIRouter()

@router.get("/ssh-test")
def ssh_test():
    return execute_command("hostname")