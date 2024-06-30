import requests


def get_all_labels(token):
    url = "https://api.todoist.com/rest/v2/labels"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def update_a_label(label_id, label_data, token):
    url = f"https://api.todoist.com/rest/v2/labels/{label_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    return requests.post(url, headers=headers, data=label_data)
