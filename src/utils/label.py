import requests
from config import BASE_URI


def get_all_labels(token, auth_type="Bearer"):
    url = f"{BASE_URI}/rest/v2/labels"
    headers = {
        'Authorization': f'{auth_type} {token}',
    }
    return requests.get(url, headers=headers)


def get_a_personal_label(token):
    url = "https://api.todoist.com/rest/v2/labels/2173775788"
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
