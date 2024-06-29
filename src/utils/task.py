import requests


def get_a_task(task_id,token):
    url = f"https://api.todoist.com/rest/v2/tasks/{task_id}"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)