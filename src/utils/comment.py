import requests


def get_comment(token):
    url = "https://api.todoist.com/rest/v2/comments/3567198885"
    headers = {
        'Authorization': f'Bearer {token}',
    }
    return requests.get(url, headers=headers)
