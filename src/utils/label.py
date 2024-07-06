import requests
from config import BASE_URI


def get_all_labels(token, auth_type="Bearer"):
    url = f"{BASE_URI}/rest/v2/labels"
    headers = {
        'Authorization': f'{auth_type} {token}',
    }
    return requests.get(url, headers=headers)


def get_a_personal_label(label_id, token):
    url = f'{BASE_URI}/rest/v2/labels/{label_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def update_a_label(label_id, label_data, token):
    url = f"{BASE_URI}/rest/v2/labels/{label_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return requests.post(url, headers=headers, data=label_data)


def delete_a_label(label_id, token):
    url = f'{BASE_URI}/rest/v2/labels/{label_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.delete(url, headers=headers)
