import requests

url = "https://api.todoist.com/rest/v2/labels/2173775788"

payload = {}
headers = {
    'Authorization': 'Bearer ec89cb82258d5f39de31b4850fa1505b214e2581',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)