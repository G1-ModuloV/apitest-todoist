import requests

def update_a_task(task_id, payload, token):
  url = f"https://api.todoist.com/rest/v2/tasks/{task_id}"
  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
  }
  return requests.request("POST", url, headers=headers, data=payload)