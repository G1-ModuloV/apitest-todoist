from config import EMAIL
from src.login import get_response_login
from src.assertions.login_assertions import assert_login_successfully


def test_tc01_login():  #Iniciar sesion con credenciales validas en el sistema todoist
    response = get_response_login()
    assert_login_successfully(response, {"full_name": "G1-Diplomado", "email": EMAIL})
