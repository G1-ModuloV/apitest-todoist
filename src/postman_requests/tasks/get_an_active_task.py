import requests

url="https://api.todoist.com/rest/v2/tasks/2995104339"

payload = {}

headers = {
    'authorization' : ' Bearer 70b0647e981e2daa4ee6c5ab66d44a34adc00536'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)