import json
import pytest
from src.utils.label import rename_share_labels, get_all_shared_labels
from src.resources.payloads.rename_share_labels_data import payload_correct, payload_bad_name, payload_bad_new_name, \
    payload_good_new_name
from src.assertions.labels.rename_shared_labels_assertions import assert_rename_share_labels_successfully, \
    assert_rename_share_labels_forbidden, assert_rename_share_labels_new_name_required, assert_a_share_label_exists, \
    assert_there_is_no_a_share_label


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("payload", payload_good_new_name)
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name validos, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name numerico, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name booleano, usando content-type correcto y un token valido.
def test_rename_shared_labels_good_new_name(payload, valid_token, setup_create_a_shared_label):
    response = rename_share_labels(json.dumps(payload), valid_token)
    assert_rename_share_labels_successfully(response)
    share_labels = get_all_shared_labels(valid_token).json()
    assert_a_share_label_exists(payload["new_name"], share_labels)


@pytest.mark.regression
@pytest.mark.parametrize("payload", payload_bad_name)
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name inexistente, new_name valido, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name numerico, new_name valido, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name booleano, new_name valido, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de new_name valido, sin name, usando content-type correcto y un token valido.
def test_rename_shared_labels_bad_name(payload, valid_token):
    response = rename_share_labels(json.dumps(payload), valid_token)
    assert_rename_share_labels_successfully(response)
    share_labels = get_all_shared_labels(valid_token).json()
    assert_there_is_no_a_share_label(payload["new_name"], share_labels)


@pytest.mark.regression
@pytest.mark.parametrize("payload", payload_bad_new_name)
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name valido, new_name vacio, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name valido, sin new_name, usando content-type correcto y un token valido.
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de un payload vacio, usando content-type correcto y un token valido.
def test_rename_shared_labels_bad_new_name(payload, valid_token):
    response = rename_share_labels(json.dumps(payload), valid_token)
    assert_rename_share_labels_new_name_required(response)


@pytest.mark.regression
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name validos, usando content-type incorrecto y un token valido.
def test_rename_shared_labels_bad_content_type(valid_token):
    response = rename_share_labels(json.dumps(payload_correct), valid_token, "text/plain")
    assert_rename_share_labels_new_name_required(response)


@pytest.mark.regression
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name validos, usando content-type incorrecto y un token invalido.
def test_rename_shared_labels_bad_content_type_bad_token(invalid_token):
    response = rename_share_labels(json.dumps(payload_correct), invalid_token, "text/plain")
    assert_rename_share_labels_forbidden(response)


@pytest.mark.regression
# TD-50 Verificar el cambio de nombre de una etiqueta compartida a partir de name y new_name validos, usando content-type correcto y un token invalido.
def test_rename_shared_labels_bad_token(invalid_token):
    response = rename_share_labels(json.dumps(payload_correct), invalid_token)
    assert_rename_share_labels_forbidden(response)
