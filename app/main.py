from fastapi import FastAPI

from app.routes import (
    automation,
    correction,
    foundry,
    ansible,
    validator,
    rollback
)


app = FastAPI(
    title="AI Ansible Automation Platform",
    description="Automated Ansible playbook generation, validation, correction and rollback",
    version="1.0.0"
)


app.include_router(
    automation.router
)

app.include_router(
    correction.router
)

app.include_router(
    foundry.router
)

app.include_router(
    ansible.router
)

app.include_router(
    validator.router
)

app.include_router(
    rollback.router
)


@app.get("/")
def root():

    return {
        "message": "AI Ansible Automation Platform is running"
    }