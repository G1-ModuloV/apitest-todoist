from src.utils.section import get_section_by_id


def assert_status_code(response, expected_code):
    assert response.status_code == expected_code


def assert_response_empty(response):
    assert response.text == ""


def assert_section_exists(section_id, token):
    response = get_section_by_id(token, section_id)
    assert response.status_code == 200
    assert response.json().get("id") == section_id

