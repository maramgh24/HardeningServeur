from app.services.ssh_service import execute_command


def create_backup():

    command = """
    sudo tar -czf /tmp/server_backup.tar.gz /etc
    """

    result = execute_command(command)

    return {
        "status": result.get("returncode", 1),
        "stdout": result["stdout"],
        "stderr": result["stderr"]
    }



def rollback():

    command = """
    sudo tar -xzf /tmp/server_backup.tar.gz -C /
    """

    result = execute_command(command)

    return {
        "status": result.get("returncode", 1),
        "stdout": result["stdout"],
        "stderr": result["stderr"]
    }