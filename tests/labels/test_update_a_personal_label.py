import json
import pytest
from src.utils.label import update_a_label
from src.resources.payloads.update_a_personal_label_data import label_id, incorrect_label_id, label_data, label_data2, \
    correct_payload, bad_payload, bad_argument, bad_color
from src.assertions.labels.update_a_personal_label_assertions import assert_update_a_label_case_one, \
    assert_update_a_label_not_found, assert_update_a_label_name_already_exists, assert_update_a_label_empty_payload, \
    assert_update_a_label_invalid_argument_value, assert_update_a_label_color_format_not_valid


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("payload", correct_payload)
# TD-26 Validar la actualización de una etiqueta solamente con el atributo "name"
# TD-26 Validar la actualización de una etiqueta solamente con el atributo "order"
# TD-26 Validar la actualización de una etiqueta solamente con el atributo "color"
# TD-26 Validar la actualización de una etiqueta solamente con el atributo "is_favorite"
# TD-26 Validar la actualización de una etiqueta con todos los atributos
def test_update_a_label_correct_payload(payload, valid_token):
    response = update_a_label(label_id, json.dumps(payload), valid_token)
    assert_update_a_label_case_one(response, payload)


@pytest.mark.regression
# TD-26 Validar la no actualización de una etiqueta a partir de un id invalido
def test_update_a_label_incorrect_id(valid_token):
    response = update_a_label(incorrect_label_id, json.dumps(label_data), valid_token)
    assert_update_a_label_not_found(response)


@pytest.mark.regression
# TD-26 Validar la no actualización de una etiqueta con un nombre que ya tiene otra etiqueta
def test_update_a_label_name_already_exists(valid_token):
    response = update_a_label(label_id, json.dumps(label_data2), valid_token)
    assert_update_a_label_name_already_exists(response)


@pytest.mark.regression
@pytest.mark.parametrize("payload", bad_payload)
# TD-26 Validar la no actualización de una etiqueta con información vacía
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "order" con valor False
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "is_favorite" con valor False
def test_update_a_label_bad_payload(payload, valid_token):
    response = update_a_label(label_id, json.dumps(payload), valid_token)
    assert_update_a_label_empty_payload(response)


@pytest.mark.regression
@pytest.mark.parametrize("payload", bad_argument)
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "name" con valor booleano
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "name" con valor numérico
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "order" con valor string
def test_update_a_label_bad_argument_value(payload, valid_token):
    response = update_a_label(label_id, json.dumps(payload), valid_token)
    assert_update_a_label_invalid_argument_value(response)


@pytest.mark.regression
@pytest.mark.parametrize("payload", bad_color)
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "color" con valor True
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "color" con valor numérico
# TD-26 Validar la no actualización de una etiqueta solamente con el atributo "color" con valor que no existe
def test_update_a_label_bad_color_format(payload, valid_token):
    response = update_a_label(label_id, json.dumps(payload), valid_token)
    assert_update_a_label_color_format_not_valid(response)
