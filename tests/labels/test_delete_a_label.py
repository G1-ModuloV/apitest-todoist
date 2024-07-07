import pytest
from src.utils.label import delete_a_label
from src.assertions.labels.delete_a_label_assertions import assert_delete_a_label_successfully, \
    assert_delete_a_label_forbidden


@pytest.mark.smoke
@pytest.mark.regression
# TD-45 Verificar la eliminacion de una etiqueta con un id valido y un token de autenticación valido
def test_delete_a_label_valid_case(get_valid_label_id, valid_token):
    response = delete_a_label(get_valid_label_id, valid_token)
    assert_delete_a_label_successfully(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-45 Verificar la eliminacion de una etiqueta con un id invalido y un token de autenticación invalido
def test_delete_a_label_invalid_case(nonexistent_label_id, invalid_token):
    response = delete_a_label(nonexistent_label_id, invalid_token)
    assert_delete_a_label_forbidden(response)