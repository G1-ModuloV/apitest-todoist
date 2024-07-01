import pytest
from src.login import get_token

#Get a project
@pytest.fixture
def valid_project_id():
    return "2335308589"


@pytest.fixture
def invalid_project_id():
    return "!3$%12"


@pytest.fixture
def nonexistent_project_id():
    return "3332123"


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
    return "4b135b0ba9400ccb273f849444ec605d2e6b8500"


@pytest.fixture
def no_token():
    return None

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

# Get All Comments
@pytest.fixture
def all_comments_valid_project_id():
    return "2335308589"

@pytest.fixture
def all_comments_valid_task_id():
    return "2335320398"

@pytest.fixture
def all_comments_invalid_id():
    return "98u234jnfk"

@pytest.fixture
def all_comments_deleted_project_id():
    return "2335509282"

@pytest.fixture
def all_comments_deleted_task_id():
    return "8164848731"

