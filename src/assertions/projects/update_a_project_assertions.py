from src.resources.payloads.update_a_project_data import (new_color, new_name, new_favorite, new_style,
                                                          data_new)


def assert_status_code(response, expected_status):
    assert response.status_code == expected_status


def assert_cambio_de_parametros(response):
    json_response = response.json()
    assert json_response["name"] == data_new["name"]
    assert json_response["color"] == data_new["color"]
    assert json_response["is_favorite"] == data_new["is_favorite"]
    assert json_response["view_style"] == data_new["view_style"]


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
