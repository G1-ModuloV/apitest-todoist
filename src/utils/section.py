import requests
from config import BASE_URI


def get_section_by_id(token, section_id):
    url = f"{BASE_URI}/rest/v2/sections/{section_id}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    return requests.get(url, headers=headers)


def post_a_section_and_get_section_id(token, project_id, name):
    url = f"{BASE_URI}/rest/v2/sections"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    payload = {
        "project_id": project_id,
        "name": name
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        section_id = response.json().get('id')
        return section_id
    else:
        response.raise_for_status()
    return response


def delete_a_section(token, section_id):
    url = f'{BASE_URI}/rest/v2/sections/{section_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    response = requests.delete(url, headers=headers)
    return response
