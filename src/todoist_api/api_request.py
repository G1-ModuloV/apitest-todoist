import requests


class TodoistRequest:
    @staticmethod
    def get(url, headers):
        return requests.get(url, headers=headers)

    @staticmethod
    def post(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)

    @staticmethod
    def update(url, headers, payload):
        return requests.post(url, headers=headers, data=payload)

    @staticmethod
    def delete(url, headers):
        return requests.delete(url, headers=headers)
