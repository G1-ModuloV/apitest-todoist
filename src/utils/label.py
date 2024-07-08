from config import BASE_URI
from src.todoist_api.api_request import TodoistRequest
from src.todoist_api.endpoint import Endpoint


def get_all_labels(token, auth_type="Bearer"):
    url = f"{BASE_URI}{Endpoint.LABELS.value}"
    headers = {
        'Authorization': f'{auth_type} {token}',
    }
    return TodoistRequest.get(url, headers)


def get_a_personal_label(label_id, token):
    url = f'{BASE_URI}{Endpoint.LABELS.value}{label_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.get(url, headers)


def update_a_label(label_id, label_data, token):
    url = f"{BASE_URI}{Endpoint.LABELS.value}{label_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.update(url, headers, label_data)


def delete_a_label(label_id, token):
    url = f'{BASE_URI}{Endpoint.LABELS.value}{label_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.delete(url, headers)


def create_a_personal_label(label_data, token):
    url = f'{BASE_URI}{Endpoint.LABELS.value}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.post(url, headers, label_data)


def get_all_shared_labels(token, auth_type="Bearer"):
    url = f"{BASE_URI}{Endpoint.SHARED_LABELS.value}"
    headers = {
        'Authorization': f'{auth_type} {token}',
    }
    return TodoistRequest.get(url, headers)


def rename_share_labels(label_data, token, content_type="application/json"):
    url = f"{BASE_URI}{Endpoint.RENAME_SHARED_LABELS.value}"
    headers = {
        'Content-Type': content_type,
        'Authorization': f'Bearer {token}',
    }
    return TodoistRequest.update(url, headers, label_data)
