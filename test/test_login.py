import pytest
import requests

def test_tc01_login(): #Iniciar sesion con credenciales validas en el sistema todoist
    email = "g1diplomado01@gmail.com"
    password = "external123"
    url = "https://app.todoist.com/api/v9.1/user/login"
    payload = {
        "email": email,
        "password": password,
        "device_id": "49880f2c-036a-67ca-18e2-5efb3ffe8286",
        "permanent_login": True,
        "pkce_oauth": None,
        "web_session": True
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'es-BO,es-419;q=0.9,es;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': '_ga=GA1.1.534901237.1718844723; csrf=c10d1382a3404e6e83a5ca73c3c63086; ps_mode=trackingV1; _ga=GA1.3.534901237.1718844723; _gid=GA1.3.545399017.1719419108; _clck=oz1rcq%7C2%7Cfmy%7C0%7C1638; _clsk=1d8bs33%7C1719419698324%7C1%7C1%7Cr.clarity.ms%2Fcollect; _ga_47KPF4T19V=GS1.1.1719419696.1.1.1719419719.0.0.0; _ga_3WJ7YJ0FM2=GS1.1.1719419696.1.1.1719419719.0.0.0; ki_r=aHR0cHM6Ly90b2RvaXN0LmNvbS8%3D; _rdt_uuid=1718844751377.5c9ea80a-6578-4c6d-be03-8b96057858e4; ki_t=1718844755162%3B1719419107997%3B1719423476583%3B4%3B21; todoistd="/CUdA09psYiwY7pwgn9sRGC/RQQ=?"; _ga_M6V9BEQD2J=GS1.1.1719422136.7.1.1719424544.0.0.0; tduser=v4.public.eyJ1c2VyX2lkIjogNDk2OTYzNTIsICJleHAiOiAiMjAyNC0wNy0xMFQxODoyOTozOCswMDowMCJ9F-rxlGeqk1HfAUh6RhSsRTdIXY1Cxij6FF0Pd6budi-8mdi9TaATCT8d-chLEXcyf7Z9EgqQF7oCCW0tQlCsAw; todoistd="qjgiSFpxLw2boMDWXM8hh6y1v1o=?pCHK=gASVJAAAAAAAAACMIGZhODY1ZDFkODM4ZDc0YTYxYTAxMGNiNDA5MDA5YjdklC4=&user_id=gASVBgAAAAAAAABKYE72Ai4="',
        'doist-locale': 'es-BO',
        'doist-os': 'Windows',
        'doist-platform': 'web',
        'doist-screen': '1920x1040',
        'doist-version': '6255',
        'origin': 'https://app.todoist.com',
        'priority': 'u=1, i',
        'referer': 'https://app.todoist.com/auth/login',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.post(url, json=payload, headers=headers)
    response_data= response.json()
    assert response.status_code == 200
    assert response_data['full_name'] == "G1-Diplomado"
    assert response_data['email'] == email
    assert response_data['token'] is not None