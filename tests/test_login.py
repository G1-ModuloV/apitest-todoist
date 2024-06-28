import pytest
import requests
from config import BASE_URI, EMAIL, PASSWORD
from src.login import get_response_login, get_token
def test_tc01_login(): #Iniciar sesion con credenciales validas en el sistema todoist
    response = get_response_login()
    assert response['full_name'] == "G1-Diplomado"
    assert response['email'] == EMAIL
    assert response['token'] is not None
