from app.services.foundry_service import generate_ansible_playbook
from app.services.validator_service import validate_yaml
from app.services.file_service import save_playbook
from app.services.ssh_service import upload_file
from app.services.ansible_service import execute_playbook
from app.services.correction_service import correct_playbook
from app.services.rollback_service import create_backup, rollback


def run_automation(configuration: str):

    # 1. Génération du playbook
    playbook = generate_ansible_playbook(configuration)

    file_path = save_playbook(playbook)

    # 2. Validation YAML
    yaml_validation = validate_yaml(playbook)

    # 3. Upload vers la VM
    upload = upload_file(
        file_path,
        "/home/maram/playbook.yml"
    )

    # 4. Création du backup avant modification
    backup = create_backup()

    # Initialisation des variables
    correction = None
    correction_validation = None
    correction_upload = None
    correction_execution = None
    rollback_result = None

    automation_status = "SUCCESS"


    # 5. Première exécution
    execution = execute_playbook(
        "/home/maram/playbook.yml"
    )


    # 6. Correction automatique si échec
    if execution["status"] != 0:

        correction = correct_playbook(
            playbook,
            execution["stderr"] + execution["stdout"]
        )


        # 7. Validation de la correction
        correction_validation = validate_yaml(correction)


        # 8. Sauvegarde du playbook corrigé
        correction_file = save_playbook(correction)


        # 9. Upload du playbook corrigé
        correction_upload = upload_file(
            correction_file,
            "/home/maram/playbook_corrected.yml"
        )


        # 10. Ré-exécution du playbook corrigé
        correction_execution = execute_playbook(
            "/home/maram/playbook_corrected.yml"
        )


        # 11. Vérification du résultat après correction
        if correction_execution["status"] == 0:

            automation_status = "SUCCESS_AFTER_CORRECTION"


        else:

            # 12. Rollback si la correction échoue
            rollback_result = rollback()

            automation_status = "ROLLBACK_EXECUTED"



    return {
        "playbook": playbook,

        "yaml_validation": yaml_validation,

        "upload": upload,

        "execution": execution,


        "correction": correction,

        "correction_validation": correction_validation,

        "correction_upload": correction_upload,

        "correction_execution": correction_execution,


        "backup": backup,

        "rollback": rollback_result,


        "automation_status": automation_status
    }