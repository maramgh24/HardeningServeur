from app.services.ssh_service import execute_command


def check_ansible_playbook(playbook_path: str):

    command = f"""
    ansible-playbook --syntax-check {playbook_path}
    """

    result = execute_command(command)

    if result["stderr"] == "":

        return {
            "valid": True,
            "stdout": result["stdout"]
        }

    return {
        "valid": False,
        "stderr": result["stderr"]
    }



def execute_playbook(playbook_path):

    command = f"""
    cd ~/ansible &&
    ansible-playbook -i inventory.ini {playbook_path}
    """

    result = execute_command(command)

    return {
        "status": result.get("returncode", 1),
        "stdout": result["stdout"],
        "stderr": result["stderr"]
    }