import pytest
from src.utils.label import delete_a_label
from src.assertions.labels.delete_a_personal_label_assertions import assert_delete_a_label_successfully, \
    assert_delete_a_label_forbidden
import requests
from src.utils.url import label_url


@pytest.mark.smoke
@pytest.mark.regression
# TD-45 Verificar la eliminación de una etiqueta con un id valido y un token de autenticación valido
def test_delete_a_label_valid_case(setup_create_a_label, valid_token):
    response = delete_a_label(setup_create_a_label, valid_token)
    assert_delete_a_label_successfully(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-45 Verificar la eliminación de una etiqueta con un id invalido y un token de autenticación invalido
def test_delete_a_label_invalid_case(nonexistent_label_id, invalid_token):
    response = delete_a_label(nonexistent_label_id, invalid_token)
    assert_delete_a_label_forbidden(response)


@pytest.mark.regression
# TD-45 Verificar la eliminación de una etiqueta con un id valido y un token de autenticación invalido
def test_delete_a_label_bad_token(setup_create_a_label, invalid_token):
    response = delete_a_label(setup_create_a_label, invalid_token)
    assert_delete_a_label_forbidden(response)


@pytest.mark.regression
# TD-45 Verificar la eliminación de una etiqueta con un id invalido y un token de autenticación valido
def test_delete_a_label_bad_id(nonexistent_label_id, valid_token):
    response = delete_a_label(nonexistent_label_id, valid_token)
    assert_delete_a_label_successfully(response)


@pytest.mark.regression
# TD-45 Verificar la eliminación de una etiqueta con un id valido y ningun tipo de autenticación
def test_delete_a_label_without_authorization(setup_create_a_label):
    response = requests.delete(label_url(setup_create_a_label), headers={})
    assert_delete_a_label_forbidden(response)
