from src.utils.project import get_a_project


def assert_status_code(response, expected_status):
    assert response.status_code == expected_status


def assert_empty_data(response):
    assert response.text == ''


def assert_name_no_exist(response):
    json_data = response.json()
    assert "name" in json_data
    assert json_data["name"] == ""
