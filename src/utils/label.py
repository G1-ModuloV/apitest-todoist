import requests


def get_all_labels(token):
    url = "https://api.todoist.com/rest/v2/labels"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
