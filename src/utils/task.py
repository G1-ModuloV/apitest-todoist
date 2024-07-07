import requests
from config import BASE_URI


def get_a_task(task_id, token):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def create_task(task_data, token):
    url = f"{BASE_URI}/rest/v2/tasks"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    return requests.post(url, headers=headers, json=task_data)


def delete_task(task_id, token):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.delete(url, headers=headers)
