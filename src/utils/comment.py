import requests
from config import URI


def get_all_comments(token):
    url = "https://api.todoist.com/rest/v2/comments?task_id=8157452578"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)


def get_a_comment(token, comment_id):
    url = f'{URI}/{comment_id}'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
