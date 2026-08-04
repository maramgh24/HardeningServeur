import yaml


def validate_yaml(playbook_content: str):

    try:
        yaml.safe_load(playbook_content)

        return {
            "valid": True,
            "message": "YAML syntax is valid"
        }

    except yaml.YAMLError as e:

        return {
            "valid": False,
            "message": "Invalid YAML",
            "error": str(e)
        }