import requests

url = "https://api.todoist.com/rest/v2/tasks"

payload = {}
headers = {
  'Authorization': 'Bearer 2a0369b3b4434f82c8d39a6bcc8ca462d7624990',
  'Cookie': 'tduser=v4.public.eyJ1c2VyX2lkIjogNDk2NzMxNTksICJleHAiOiAiMjAyNC0wNy0xOFQyMzoxNDoxNyswMDowMCJ9MGunMpC63qvJF5ozfTph2FSuUN04BwZY5JsHdd4y695Fb4T6KbYGOsB9dUYnmGXC-Biw1w4yvIDq-s5pq9TUBQ; todoistd="/CUdA09psYiwY7pwgn9sRGC/RQQ=?"; csrf=4c4ccaaa136842889a76406b5b6ad624'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)