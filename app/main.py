from fastapi import FastAPI

from app.routes import foundry
from app.routes import ansible
from app.routes import validator
from app.routes import ansible_validator
from app.routes import automation
from app.routes import ssh_test
from app.routes import upload_test
from app.routes import correction


app = FastAPI(
    title="AI Ansible Automation",
    version="1.0"
)


app.include_router(foundry.router)

app.include_router(ansible.router)

app.include_router(validator.router)

app.include_router(ansible_validator.router)

app.include_router(automation.router)

app.include_router(ssh_test.router)

app.include_router(upload_test.router)

app.include_router(correction.router)



@app.get("/")
def home():

    return {
        "message":"Backend is running"
    }