from fastapi import APIRouter
from app.services.ssh_service import upload_file


router = APIRouter()


@router.post("/upload-test")
def upload_test():

    result = upload_file(
        "generated_playbooks/playbook_test.yml",
        "/home/maram/playbook_test.yml"
    )

    return result