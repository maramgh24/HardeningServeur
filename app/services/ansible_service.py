
from app.services.ssh_service import execute_command


def check_ansible_playbook(playbook_path: str):

    command = (
        f"ansible-playbook "
        f"-i /home/maram/inventory "
        f"--syntax-check "
        f"{playbook_path}"
    )

    result = execute_command(command)

    if result.get("returncode", 1) == 0:

        return {
            "valid": True,
            "stdout": result.get("stdout", ""),
            "stderr": result.get("stderr", "")
        }

    return {
        "valid": False,
        "stdout": result.get("stdout", ""),
        "stderr": result.get("stderr", "")
    }


def execute_playbook(playbook_path: str, environment: str):

    if environment not in ["test", "prod"]:

        return {
            "status": 1,
            "stdout": "",
            "stderr": "Invalid environment. Use 'test' or 'prod'."
        }

    command = (
        f"ansible-playbook "
        f"-i /home/maram/inventory "
        f"{playbook_path} "
        f"--limit {environment}"
    )

    result = execute_command(command)

    return {
        "status": result.get("returncode", 1),
        "stdout": result.get("stdout", ""),
        "stderr": result.get("stderr", "")
    }
