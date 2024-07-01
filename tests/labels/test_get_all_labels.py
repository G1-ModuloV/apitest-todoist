import requests
import pytest
from src.login import get_token
from src.utils.label import get_all_labels
from src.assertions.labels.get_all_labels_assertions import assert_get_all_labels_case_one, \
    assert_get_all_labels_forbidden, assert_get_all_labels_invalid_format
from config import BASE_URI


@pytest.mark.smoke
def test_get_all_labels():
    response = get_all_labels(get_token())
    assert_get_all_labels_case_one(response)


def test_get_all_labels_empty_token():
    response = get_all_labels("")
    assert_get_all_labels_invalid_format(response)


def test_get_all_labels_bad_token(invalid_token):
    response = get_all_labels(invalid_token)
    assert_get_all_labels_forbidden(response)


def test_get_all_labels_without_authorization():
    response = requests.get(f"{BASE_URI}/rest/v2/labels", headers={})
    assert_get_all_labels_forbidden(response)


def test_get_all_labels_api_key_authorization():
    response = get_all_labels(get_token(), "APIkey")
    assert_get_all_labels_invalid_format(response)


def test_get_all_labels_basic_authorization():
    response = get_all_labels(get_token(), "Basic")
    assert_get_all_labels_invalid_format(response)
