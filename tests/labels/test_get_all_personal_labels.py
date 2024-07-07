import requests
import pytest
from src.utils.label import get_all_labels
from src.assertions.labels.get_all_labels_assertions import assert_get_all_labels_case_one, \
    assert_get_all_labels_forbidden, assert_get_all_labels_invalid_format
from config import BASE_URI


@pytest.mark.smoke
@pytest.mark.regression
# TD-27 Validar la obtención de las etiquetas usando la autenticación de tipo Bearer con token correcto
def test_get_all_labels(valid_token):
    response = get_all_labels(valid_token)
    assert_get_all_labels_case_one(response)


@pytest.mark.regression
# TD-27 Validar la obtención de las etiquetas usando la autenticación de tipo Bearer con token vacio
def test_get_all_labels_empty_token():
    response = get_all_labels("")
    assert_get_all_labels_invalid_format(response)


@pytest.mark.regression
# TD-27 Validar la obtención de las etiquetas usando la autenticación de tipo Bearer con token incorrecto
def test_get_all_labels_bad_token(invalid_token):
    response = get_all_labels(invalid_token)
    assert_get_all_labels_forbidden(response)


@pytest.mark.regression
# TD-27 Validar la no obtención de las etiquetas usando ningun tipo de autenticación
def test_get_all_labels_without_authorization():
    response = requests.get(f"{BASE_URI}/rest/v2/labels", headers={})
    assert_get_all_labels_forbidden(response)


@pytest.mark.regression
# TD-27 Validar la no obtención de las etiquetas usando la autenticación de tipo APIKey
def test_get_all_labels_api_key_authorization(valid_token):
    response = get_all_labels(valid_token, "APIkey")
    assert_get_all_labels_invalid_format(response)


@pytest.mark.regression
# TD-27 Validar la no obtención de las etiquetas usando la autenticación de tipo Basic
def test_get_all_labels_basic_authorization(valid_token):
    response = get_all_labels(valid_token, "Basic")
    assert_get_all_labels_invalid_format(response)
