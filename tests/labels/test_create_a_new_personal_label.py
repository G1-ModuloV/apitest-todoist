import pytest
import json
from src.utils.label import (create_a_personal_label, get_a_personal_label, get_create_a_personal_label,
                             create_a_personal_label_incorrect_header)
from src.resources.payloads.create_label_data import label_data, empty_data, invalid_data
from src.assertions.labels.create_a_new_personal_label_assertion import (assert_post_create_a_personal_label_name_valid,
                                                                         assert_post_create_a_personal_label_invalid_token,
                                                                         assert_post_create_a_personal_label_invalid_data,
                                                                         assert_get_create_a_personal_label)


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con un nombre valido
def test_create_a_personal_label_valid_name(setup_create_personal_label, valid_token):
    response = get_a_personal_label(setup_create_personal_label, valid_token)
    assert_post_create_a_personal_label_name_valid(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con nombre y datos opcionales
def test_create_a_personal_label_all_valid(setup_create_personal_label_all_valid, valid_token):
    response = get_a_personal_label(setup_create_personal_label_all_valid, valid_token)
    assert_post_create_a_personal_label_name_valid(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-24 Crea una etiqueta con un nombre y marcado como favorito
def test_create_a_personal_label_is_favorite(setup_create_personal_label_is_favorite, valid_token):
    response = get_a_personal_label(setup_create_personal_label_is_favorite, valid_token)
    assert_post_create_a_personal_label_name_valid(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un token invalido 401
def test_create_a_personal_label_invalid_token(invalid_token):
    response = create_a_personal_label(json.dumps(label_data), invalid_token)
    assert_post_create_a_personal_label_invalid_token(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un token vacio 401
def test_create_a_personal_label_invalid_token(no_token):
    response = create_a_personal_label(json.dumps(label_data), no_token)
    assert_post_create_a_personal_label_invalid_token(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un formato de cuerpo incorrecto 400
def test_create_a_personal_label_invalid_data_body(valid_token):
    response = create_a_personal_label(json.dumps(invalid_data), valid_token)
    assert_post_create_a_personal_label_invalid_data(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un label con un formato de cuerpo vacio 400
def test_create_a_personal_label_invalid_data_body(valid_token):
    response = create_a_personal_label(json.dumps(empty_data), valid_token)
    assert_post_create_a_personal_label_invalid_data(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear con un verbo incorrecto error 403
def test_get_create_a_personal_label(valid_token):
    response = get_create_a_personal_label(json.dumps(label_data), valid_token)
    assert_get_create_a_personal_label(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un etiqueta con el mismo nombre de otra etiqueta activa error 400
def test_get_create_a_personal_label_duplicate_name(setup_create_personal_label_all_valid, valid_token):
    response = create_a_personal_label(json.dumps(label_data), valid_token)
    assert_post_create_a_personal_label_invalid_data(response)


@pytest.mark.regression
# TD-24 Verificar la respuesta al intentar crear un etiqueta con el mismo nombre de otra etiqueta activa error 400
def test_get_create_a_personal_label_incorrect_header(valid_token):
    response = create_a_personal_label_incorrect_header(json.dumps(label_data), valid_token)
    assert_post_create_a_personal_label_invalid_data(response)
