from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import (
    automation,
    correction,
    foundry,
    ansible,
    validator,
    rollback,
    stats
)


app = FastAPI(
    title="AI Ansible Automation Platform",
    description="Automated Ansible playbook generation, validation, correction and rollback",
    version="1.0.0"
)


# ==================================================
# CORS
# ==================================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
# ==================================================
# ROUTES
# ==================================================

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

app.include_router(
    stats.router
)


# ==================================================
# ROOT
# ==================================================

@app.get("/")
def root():

    return {
        "message": "AI Ansible Automation Platform is running"
    }