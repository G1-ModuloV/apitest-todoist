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

#Get a Comment
@pytest.fixture
def valid_comment_id():
    return "3567198885"

@pytest.fixture
def null_comment_id():
    return None

@pytest.fixture
def invalid_comment_id():
    return "invalid_comment_id"



# Get an active task
@pytest.fixture
def valid_task_id():
    return "8160389085"

@pytest.fixture
def invalid_task_id():
    return "invalid_task_id"


@pytest.fixture
def non_existent_task_id():
    return "9999999999"

@pytest.fixture
def deleted_task_id():
    return "8164612172"

@pytest.fixture
def null_task_id():
    return None
