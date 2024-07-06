
def assert_status_code(response,aux):
    assert response.status_code == aux

def assert_cambio_de_parametros(response):
    json_response = response.json()
    assert json_response["name"] == "Automatizar project"
    assert json_response["color"] == "red"
    assert json_response["is_favorite"] == False
    assert json_response["view_style"] == "list"

def assert_name (response):
    json_response = response.json()
    assert json_response["name"] == "New Project Name"

def assert_color (response):
    json_response = response.json()
    assert json_response["color"] == "yellow"

def assert_favorite(response):
    json_response = response.json()
    assert json_response["color"] == "red"
    assert json_response["is_favorite"] == False

def assert_style(response):
    json_response = response.json()
    assert json_response["view_style"] == "board"