import requests
from config import BASE_URI


def get_all_labels(token):
    url = "https://api.todoist.com/rest/v2/labels"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def get_a_personal_label(label_id, token):
    url = f'{BASE_URI}/rest/v2/labels/{label_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
