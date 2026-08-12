from pathlib import Path
from datetime import datetime


PLAYBOOK_DIR = Path("generated_playbooks")


def save_playbook(playbook: str) -> str:
    PLAYBOOK_DIR.mkdir(exist_ok=True)

    filename = (
        f"playbook_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.yml"
    )

    file_path = PLAYBOOK_DIR / filename

    file_path.write_text(
        playbook,
        encoding="utf-8"
    )

    return str(file_path)


def save_corrected_playbook(playbook: str) -> str:
    PLAYBOOK_DIR.mkdir(exist_ok=True)

    filename = (
        f"corrected_playbook_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.yml"
    )

    file_path = PLAYBOOK_DIR / filename

    file_path.write_text(
        playbook,
        encoding="utf-8"
    )

    return str(file_path)