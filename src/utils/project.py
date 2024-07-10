import requests
from config import BASE_URI
from src.resources.payloads.create_a_project_data import get_project_data


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


def post_a_project_with_id(token, project_id):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URI}/rest/v2/projects/{project_id}"
    response = requests.post(url, headers=headers)
    return response


def post_a_project_with_using_get(token, project_id):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URI}/rest/v2/projects/{project_id}"
    response = requests.get(url, headers=headers)
    return response


def post_a_project_with_wrong_content_type(token, project_id):
    data = get_project_data("valid_name")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "text/plain"
    }
    url = f"{BASE_URI}/rest/v2/projects/{project_id}"
    response = requests.post(url, headers=headers, data=data)
    return response


def post_a_project_with_data_invalid(token, project_id):
    data = "invalid_body_format"
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URI}/rest/v2/projects/{project_id}"
    response = requests.post(url, headers=headers, data=data)
    return response


def post_a_project(token, data):
    url = f"{BASE_URI}/rest/v2/projects/"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(url, headers=headers, json=data)
    return response


def update_a_project(project_id_update, project_data, token):
    url = f"{BASE_URI}/rest/v2/projects/{project_id_update}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return requests.post(url, headers=headers, data=project_data)


def delete_a_project(token, project_id):
    url = f"{BASE_URI}/rest/v2/projects/{project_id}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    return requests.delete(url, headers=headers)
