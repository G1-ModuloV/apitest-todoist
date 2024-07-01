import requests
from config import BASE_URI


def get_all_comments_from_task(token, task_id):
    url = f'{BASE_URI}/rest/v2/comments?task_id={task_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def get_a_comment(token, comment_id):
    url = f'{BASE_URI}/rest/v2/comments/{comment_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)

def get_all_comments_from_project(token, project_id):
    url = f'{BASE_URI}/rest/v2/comments?project_id={project_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
