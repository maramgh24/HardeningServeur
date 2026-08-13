from app.services.foundry_service import generate_ansible_playbook
from app.services.validator_service import validate_yaml
from app.services.file_service import save_playbook
from app.services.ssh_service import upload_file
from app.services.ansible_service import execute_playbook
from app.services.rollback_service import create_backup
from app.services.stats_service import stats_service


def run_automation(
    configuration: str,
    environment: str
):

    # ==================================================
    # 1. Génération du playbook
    # ==================================================

    playbook = generate_ansible_playbook(configuration)

    file_path = save_playbook(playbook)


    # ==================================================
    # 2. Validation YAML
    # ==================================================

    yaml_validation = validate_yaml(playbook)

    if not yaml_validation["valid"]:

        stats_service.record_automation(
            success=False
        )

        return {
            "automation_status": "YAML_ERROR",
            "environment": environment,
            "playbook": playbook,
            "yaml_validation": yaml_validation
        }


    # ==================================================
    # 3. Upload du playbook
    # ==================================================

    try:

        upload = upload_file(
            file_path,
            "/home/maram/playbook.yml"
        )

    except Exception as e:

        stats_service.record_automation(
            success=False
        )

        return {
            "automation_status": "UPLOAD_ERROR",
            "environment": environment,
            "playbook": playbook,
            "yaml_validation": yaml_validation,
            "error": str(e)
        }


    # ==================================================
    # 4. Création du backup
    # ==================================================

    backup = create_backup()


    # ==================================================
    # 5. Exécution du playbook
    # ==================================================

    try:

        execution = execute_playbook(
            "/home/maram/playbook.yml",
            environment
        )

    except Exception as e:

        stats_service.record_automation(
            success=False
        )

        return {
            "automation_status": "EXECUTION_ERROR",
            "environment": environment,
            "playbook": playbook,
            "yaml_validation": yaml_validation,
            "upload": upload,
            "backup": backup,
            "error": str(e),
            "rollback": None
        }


    # ==================================================
    # 6. Échec de l'exécution
    # ==================================================

    if execution["status"] != 0:

        stats_service.record_automation(
            success=False
        )

        return {
            "automation_status": "EXECUTION_FAILED",
            "environment": environment,
            "playbook": playbook,
            "yaml_validation": yaml_validation,
            "upload": upload,
            "execution": execution,
            "backup": backup,
            "rollback": None
        }


    # ==================================================
    # 7. Succès
    # ==================================================

    stats_service.record_automation(
        success=True
    )

    return {
        "automation_status": "SUCCESS",
        "environment": environment,
        "playbook": playbook,
        "yaml_validation": yaml_validation,
        "upload": upload,
        "execution": execution,
        "backup": backup,
        "rollback": None
    }