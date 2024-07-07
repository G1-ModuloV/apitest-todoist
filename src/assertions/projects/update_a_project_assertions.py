from src.resources.payloads.update_a_project_data import new_color, new_name, new_favorite, new_style, data_origin


def assert_status_code(response, aux):
    assert response.status_code == aux


def assert_cambio_de_parametros(response):
    json_response = response.json()
    assert json_response["name"] == "Automatizar project"
    assert json_response["color"] == "red"
    assert json_response["is_favorite"] == False
    assert json_response["view_style"] == "list"


def assert_name(response):
    json_response = response.json()
    assert json_response["name"] == new_name["name"]


def assert_color(response):
    json_response = response.json()
    assert json_response["color"] == new_color["color"]


def assert_favorite(response):
    json_response = response.json()
    assert json_response["color"] == new_favorite["color"]
    assert json_response["is_favorite"] == False


def assert_style(response):
    json_response = response.json()
    assert json_response["view_style"] == new_style["view_style"]
