import json
import pytest
from src.login import get_token
from src.utils.label import update_a_label
from src.resources.payloads.update_label_data import label_id, incorrect_label_id, label_data, label_data2, \
    correct_payload, bad_payload, \
    bad_argument, bad_color
from src.assertions.labels.update_a_label_assertions import assert_update_a_label_case_one, \
    assert_update_a_label_not_found, assert_update_a_label_name_already_exists, assert_update_a_label_empty_payload, \
    assert_update_a_label_invalid_argument_value, assert_update_a_label_color_format_not_valid


@pytest.mark.smoke
@pytest.mark.parametrize("payload", correct_payload)
def test_update_a_label_correct_payload(payload):
    response = update_a_label(label_id, json.dumps(label_data), get_token())
    assert_update_a_label_case_one(response, label_data)


def test_update_a_label_incorrect_id():
    response = update_a_label(incorrect_label_id, json.dumps(label_data), get_token())
    assert_update_a_label_not_found(response)


def test_update_a_label_name_already_exists():
    response = update_a_label(label_id, json.dumps(label_data2), get_token())
    assert_update_a_label_name_already_exists(response)


@pytest.mark.parametrize("payload", bad_payload)
def test_update_a_label_bad_payload(payload):
    response = update_a_label(label_id, json.dumps(payload), get_token())
    assert_update_a_label_empty_payload(response)


@pytest.mark.parametrize("payload", bad_argument)
def test_update_a_label_bad_argument_value(payload):
    response = update_a_label(label_id, json.dumps(payload), get_token())
    assert_update_a_label_invalid_argument_value(response)


@pytest.mark.parametrize("payload", bad_color)
def test_update_a_label_bad_color_format(payload):
    response = update_a_label(label_id, json.dumps(payload), get_token())
    assert_update_a_label_color_format_not_valid(response)
