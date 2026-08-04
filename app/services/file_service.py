from pathlib import Path
from datetime import datetime


PLAYBOOK_DIR = Path("generated_playbooks")


def save_playbook(playbook: str):

    PLAYBOOK_DIR.mkdir(exist_ok=True)

    filename = f"playbook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yml"

    file_path = PLAYBOOK_DIR / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(playbook)

    return str(file_path)