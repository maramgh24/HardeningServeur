from app.services.foundry_service import generate_ansible_playbook
from app.services.validator_service import validate_yaml
from app.services.file_service import save_playbook
from app.services.ssh_service import upload_file
from app.services.ansible_service import execute_playbook
from app.services.rollback_service import create_backup


def run_automation(configuration: str, environment: str):

    # 1. Génération du playbook
    playbook = generate_ansible_playbook(configuration)

    file_path = save_playbook(playbook)

    # 2. Validation YAML
    yaml_validation = validate_yaml(playbook)

    if not yaml_validation["valid"]:
        return {
            "automation_status": "YAML_ERROR",
            "environment": environment,
            "playbook": playbook,
            "yaml_validation": yaml_validation
        }

    # 3. Upload du playbook
    upload = upload_file(
        file_path,
        "/home/maram/playbook.yml"
    )

    # 4. Création du backup
    backup = create_backup()

    # 5. Exécution dans l'environnement choisi
    execution = execute_playbook(
        "/home/maram/playbook.yml",
        environment
    )

    # 6. Échec de l'exécution
    if execution["status"] != 0:
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

    # 7. Succès
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