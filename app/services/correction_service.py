from app.services.foundry_service import (
    generate_response,
    extract_text,
    clean_yaml
)


def correct_playbook(
    playbook: str,
    error_message: str
) -> str:

    prompt = f"""
You are an expert Ansible engineer.

You must FIX the following Ansible playbook.

ORIGINAL PLAYBOOK:
{playbook}

ANSIBLE ERROR:
{error_message}

Your task is to identify the ROOT CAUSE of the error and generate
a genuinely corrected and executable Ansible playbook.

STRICT RULES:

1. Return ONLY the corrected YAML playbook.
2. Do not return Markdown.
3. Do not return explanations.
4. Do not return ```yaml.
5. The corrected playbook MUST be valid YAML.
6. The corrected playbook MUST be executable with Ansible.
7. Fix the ROOT CAUSE of the error.
8. Do NOT simply rename tasks.
9. Do NOT simply change task names.
10. Do NOT keep the invalid configuration.
11. Do NOT use ignore_errors.
12. Do NOT use failed_when: false.
13. Do NOT hide or suppress the error.
14. If a package, service, path, variable, module or value is invalid,
    replace it with a valid alternative when the error clearly allows it.
15. The corrected playbook must actually be capable of succeeding.
16. Preserve the original objective whenever possible.
17. Do not invent unavailable resources.
18. If the original requested package does not exist, replace it with
    an appropriate real package that exists on AlmaLinux/RHEL 9 when
    this is a package-installation test.
19. Do not create a correction that only skips the failed task.
20. Do not use "when: false" or equivalent tricks to avoid the error.

Return ONLY the final corrected YAML.

ORIGINAL PLAYBOOK:
{playbook}

ANSIBLE ERROR:
{error_message}
"""

    response = generate_response(prompt)

    corrected = extract_text(response)

    corrected = clean_yaml(corrected)

    return corrected