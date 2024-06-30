import requests


def get_all_labels(token):
    url = "https://api.todoist.com/rest/v2/labels"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def get_a_personal_label(token):
    url = "https://api.todoist.com/rest/v2/labels/2173775788"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)