import requests

from app.config import (
    AZURE_API_KEY,
    AZURE_ENDPOINT,
    MODEL_NAME,
    API_VERSION
)


def generate_response(prompt: str):

    url = (
        f"{AZURE_ENDPOINT}/openai/responses"
        f"?api-version={API_VERSION}"
    )

    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_API_KEY
    }

    data = {
        "model": MODEL_NAME,
        "input": prompt,
        "max_output_tokens": 2048
    }


    response = requests.post(
        url,
        headers=headers,
        json=data
    )


    if response.status_code != 200:
        raise Exception(
            f"Azure Error {response.status_code}: {response.text}"
        )


    return response.json()



def extract_text(response):

    return response["output"][0]["content"][0]["text"]



def clean_yaml(text):

    text = text.replace("```yaml", "")
    text = text.replace("```", "")

    return text.strip()



def generate_ansible_playbook(requirement: str):

    prompt = f"""

Tu es un expert Linux RHEL AlmaLinux et Ansible.

Génère un playbook Ansible YAML.

Configuration :
{requirement}

Contraintes :
- Compatible RHEL 9 / AlmaLinux 9
- Utiliser become: yes
- Retourner uniquement YAML
"""


    result = generate_response(prompt)

    playbook = extract_text(result)

    return clean_yaml(playbook)