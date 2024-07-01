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


#Get personal Label
@pytest.fixture
def invalid_label_id():
    return "invalid_label_id"

@pytest.fixture
def valid_label_id():
    return "2173790901"

@pytest.fixture
def valid_query_param_label_id():
    return "?id=2173790901"

@pytest.fixture
def deleted_label_id():
    return "2173775788"

#Post Update a Task
@pytest.fixture
def valid_task_id_2():
    return "8162142610"

@pytest.fixture
def valid_task_id_3():
    return "8164654097"

@pytest.fixture
def valid_task_payload1():
    return "{\"content\": \"Tarea 6 actualizar-100\"}"

@pytest.fixture
def valid_task_payload2():
    return "{\"description\": \"actualizando continuamente - 200\"}"

@pytest.fixture
def valid_task_payload3():
    return "{\"priority\": 1}"

@pytest.fixture
def valid_task_payload4():
    return "{\"labels\": [\"automa_00\",\"test850\"]}"

@pytest.fixture
def valid_task_payload5():
    return "{\"due_date\": \"2024-06-29\"}"

@pytest.fixture
def valid_task_payload6():
    return "{\"content\": \"8*/*98*9\"}"

@pytest.fixture
def valid_task_payload7():
    return "{\"description\": \"//*+6-.'?\"}"

@pytest.fixture
def valid_task_payload8():
    return "{\"due_date\": \"1909-06-30\"}"

