import pytest
from src.login import get_token


@pytest.fixture
def valid_project_id():
    return "2335308589"


@pytest.fixture
def invalid_project_id():
    return "invalid_project_id"


@pytest.fixture
def nonexistent_project_id():
    return "nonexistent_project_id"


@pytest.fixture
def null_project_id():
    return None


@pytest.fixture
def alphanumeric_project_id():
    return "abc123xyz"


@pytest.fixture
def valid_token():
    return get_token()


@pytest.fixture
def invalid_token():
    return "invalid_token"


@pytest.fixture
def no_token():
    return None