from app.services.foundry_service import generate_ansible_playbook
from app.services.validator_service import validate_yaml
from app.services.file_service import save_playbook
from app.services.ssh_service import upload_file
from app.services.ansible_service import execute_playbook
from app.services.correction_service import correct_playbook


def run_automation(configuration: str):

    # 1. Génération
    playbook = generate_ansible_playbook(configuration)

    file_path = save_playbook(playbook)

    # 2. Validation YAML
    yaml_validation = validate_yaml(playbook)

    # 3. Upload VM
    upload = upload_file(
        file_path,
        "/home/maram/playbook.yml"
    )

    # 4. Exécution
    execution = execute_playbook("/home/maram/playbook.yml")
    # 5. Correction automatique si erreur
    correction = None

    if execution["status"] != 0:

    # 5. Correction IA
        correction = correct_playbook(
            playbook,
            execution["stderr"] + execution["stdout"]
        )

    # 6. Validation de la correction
        correction_validation = validate_yaml(correction)

    # 7. Sauvegarde du playbook corrigé
        correction_file = save_playbook(correction)

    # 8. Upload du playbook corrigé
        correction_upload = upload_file(
            correction_file,
            "/home/maram/playbook_corrected.yml"
        )

    # 9. Ré-exécution
        correction_execution = execute_playbook(
            "/home/maram/playbook_corrected.yml"
        )

    return {
    "playbook": playbook,
    "yaml_validation": yaml_validation,
    "upload": upload,
    "execution": execution,
    "correction": correction,
    "correction_validation": correction_validation,
    "correction_upload": correction_upload,
    "correction_execution": correction_execution
    }