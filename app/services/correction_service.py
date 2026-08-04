from app.services.foundry_service import generate_response, extract_text, clean_yaml


def correct_playbook(playbook: str, error_message: str):

    prompt = f"""
You are an Ansible expert.

The following playbook contains errors.

Error:
{error_message}

Correct the playbook.

Rules:
- Return ONLY valid YAML
- Do NOT use ignore_errors
- Do NOT use failed_when: false
- Do NOT hide errors
- Apply a real correction
- Analyze the Ansible error carefully.
- Fix the root cause of the failure.
- Do not just rename tasks.
- Do not keep the same invalid configuration.
- Replace invalid values if necessary.
- Return a fully executable YAML playbook.

Playbook:
{playbook}
"""

    response = generate_response(prompt)

    corrected = extract_text(response)

    corrected = clean_yaml(corrected)

    return corrected