import requests
from config import BASE_URI


def get_a_task(task_id, token):
    url = f"{BASE_URI}/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
