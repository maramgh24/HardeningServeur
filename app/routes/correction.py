from fastapi import APIRouter

from app.services.correction_service import correct_playbook
from app.services.validator_service import validate_yaml
from app.services.file_service import save_corrected_playbook
from app.services.ssh_service import upload_file
from app.services.ansible_service import execute_playbook


print("CORRECTION ROUTE LOADED")


router = APIRouter(
    prefix="/correction",
    tags=["Correction"]
)


@router.post("/ai")
def correct_with_ai(request: dict):

    print("========== /correction/ai ==========")
    print("REQUEST =", request)

    playbook = request["playbook"]
    error = request["error"]

    correction = correct_playbook(
        playbook,
        error
    )

    print("AI CORRECTION GENERATED")

    validation = validate_yaml(correction)

    print("VALIDATION =", validation)

    if not validation["valid"]:
        return {
            "status": "YAML_ERROR",
            "correction": correction,
            "validation": validation
        }

    return {
        "status": "AI_CORRECTION_GENERATED",
        "correction": correction,
        "validation": validation
    }


@router.post("/manual")
def manual_correction(request: dict):

    print("========== /correction/manual ==========")
    print("REQUEST =", request)

    playbook = request["playbook"]

    validation = validate_yaml(playbook)

    print("VALIDATION =", validation)

    if not validation["valid"]:
        return {
            "status": "YAML_ERROR",
            "validation": validation
        }

    return {
        "status": "MANUAL_CORRECTION_VALID",
        "correction": playbook,
        "validation": validation
    }


@router.post("/accept")
def accept_correction(request: dict):

    print("========== /correction/accept ==========")
    print("REQUEST =", request)

    # --------------------------------------------------
    # 1. Récupération des données
    # --------------------------------------------------

    try:
        playbook = request["playbook"]
        environment = request["environment"]

        print("PLAYBOOK RECEIVED")
        print("ENVIRONMENT =", environment)

    except Exception as e:

        print("ERROR READING REQUEST:", str(e))

        return {
            "status": "REQUEST_ERROR",
            "error": str(e)
        }

    # --------------------------------------------------
    # 2. Vérification de l'environnement
    # --------------------------------------------------

    if environment not in ["test", "prod"]:

        print("INVALID ENVIRONMENT:", environment)

        return {
            "status": "INVALID_ENVIRONMENT",
            "message": "Environment must be 'test' or 'prod'."
        }

    # --------------------------------------------------
    # 3. Validation YAML
    # --------------------------------------------------

    try:

        validation = validate_yaml(playbook)

        print("YAML VALIDATION =", validation)

    except Exception as e:

        print("ERROR DURING YAML VALIDATION:", str(e))

        return {
            "status": "VALIDATION_ERROR",
            "error": str(e)
        }

    if not validation["valid"]:

        print("YAML IS INVALID")

        return {
            "status": "YAML_ERROR",
            "validation": validation
        }

    # --------------------------------------------------
    # 4. Sauvegarde du playbook
    # --------------------------------------------------

    try:

        file_path = save_corrected_playbook(playbook)

        print("FILE SAVED =", file_path)

    except Exception as e:

        print("ERROR SAVING FILE:", str(e))

        return {
            "status": "FILE_SAVE_ERROR",
            "error": str(e)
        }

    # --------------------------------------------------
    # 5. Upload vers la VM de contrôle
    # --------------------------------------------------

    try:

        upload = upload_file(
            file_path,
            "/home/maram/playbook_corrected.yml"
        )

        print("UPLOAD RESULT =", upload)

    except Exception as e:

        print("ERROR DURING UPLOAD:", str(e))

        return {
            "status": "UPLOAD_ERROR",
            "error": str(e)
        }

    # --------------------------------------------------
    # 6. Exécution Ansible
    # --------------------------------------------------

    try:

        execution = execute_playbook(
            "/home/maram/playbook_corrected.yml",
            environment
        )

        print("EXECUTION RESULT =", execution)

    except Exception as e:

        print("ERROR DURING ANSIBLE EXECUTION:", str(e))

        return {
            "status": "ANSIBLE_EXECUTION_ERROR",
            "error": str(e),
            "upload": upload
        }

    # --------------------------------------------------
    # 7. Résultat final
    # --------------------------------------------------

    if execution["status"] == 0:

        print("CORRECTION EXECUTED SUCCESSFULLY")

        return {
            "status": "SUCCESS_AFTER_CORRECTION",
            "environment": environment,
            "file": file_path,
            "playbook": playbook,
            "validation": validation,
            "upload": upload,
            "execution": execution
        }

    print("CORRECTION EXECUTION FAILED")

    return {
        "status": "CORRECTION_EXECUTION_FAILED",
        "environment": environment,
        "file": file_path,
        "playbook": playbook,
        "validation": validation,
        "upload": upload,
        "execution": execution
    }