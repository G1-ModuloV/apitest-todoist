import requests
from config import BASE_URI


def get_a_project(token, project_id):
    url = f'{BASE_URI}/rest/v2/projects/{project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
def get_a_project_with_invalid_url(token, project_id):
    url = f'{BASE_URI}/rest/v2/{project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def get_all_projects(token):
    url = f'{BASE_URI}/rest/v2/projects'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def post_a_project_with_id(token, project_id, endpoint="https://api.todoist.com/rest/v2/projects"):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{endpoint}/{project_id}"
    response = requests.post(url, headers=headers)
    return response


def update_a_project(project_id_update, project_data, token):
    url = f"{BASE_URI}/rest/v2/projects/{project_id_update}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return requests.post(url, headers=headers, data=project_data)