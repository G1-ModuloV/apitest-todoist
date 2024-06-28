import requests

url = "https://api.todoist.com/rest/v2/comments?task_id=8157452578"

payload = {}
headers = {
  'Authorization': 'Bearer 4b135b0ba9400ccb273f849444ec605d2e6b8500'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
