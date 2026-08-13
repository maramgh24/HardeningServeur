from app.services.ssh_service import execute_command
from app.services.stats_service import stats_service


# ==================================================
# CREATE BACKUP
# ==================================================

def create_backup():

    command = """
    sudo tar -czf /tmp/server_backup.tar.gz /etc
    """

    result = execute_command(
        command
    )

    return {
        "status": result.get(
            "returncode",
            1
        ),
        "stdout": result["stdout"],
        "stderr": result["stderr"]
    }


# ==================================================
# ROLLBACK
# ==================================================

def rollback():

    command = """
    sudo tar -xzf /tmp/server_backup.tar.gz -C /
    """

    result = execute_command(
        command
    )

    # --------------------------------------------------
    # Déterminer si le rollback a réussi
    # --------------------------------------------------

    success = (
        result.get(
            "returncode",
            1
        ) == 0
    )

    # --------------------------------------------------
    # Enregistrer les statistiques
    # UNE SEULE FOIS
    # --------------------------------------------------

    stats_service.record_rollback(
        success=success
    )

    # --------------------------------------------------
    # Retourner le résultat
    # --------------------------------------------------

    return {
        "status": result.get(
            "returncode",
            1
        ),
        "stdout": result["stdout"],
        "stderr": result["stderr"]
    }