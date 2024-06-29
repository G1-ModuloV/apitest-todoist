import requests

url = "https://api.todoist.com/rest/v2/comments/3567198885"

payload = ""
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,es;q=0.8',
  'content-type': 'text/plain',
  'priority': 'u=1, i',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'Authorization': 'Bearer 4b135b0ba9400ccb273f849444ec605d2e6b8500',
  'Cookie': 'tduser=v4.public.eyJ1c2VyX2lkIjogNDk2NzY3OTAsICJleHAiOiAiMjAyNC0wNy0wOVQwMDowNToxMCswMDowMCJ9FiVrGf5ac64DR0InDk5-9BUThzY1Ts6dz0r17mOmfJ-5YYsIPan7DoCM275YopY3GPA-d-620E8K1TWSys0tDA; todoistd="/CUdA09psYiwY7pwgn9sRGC/RQQ=?"; csrf=4b8e63ec64834d2487986f2dfd035f4b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
