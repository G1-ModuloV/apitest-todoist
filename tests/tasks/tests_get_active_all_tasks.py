import pytest
from src.utils.task import (get_tasks, get_tasks_from_project, get_tasks_from_seccion)
from src.login import get_token
from src.utils.task import get_a_task
from src.assertions.tasks.get_active_tasks_assertions import (
    assert_get_all_tasks_success,
    assert_get_all_tasks_of_project_success,
    assert_get_all_tasks_of_seccion_success,
    assert_get_all_tasks_bad_request,
    assert_get_all_tasks_unauthorized)

@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion de la lista de tareas es Exitosa con token valido - SMOKE
def test_get_active_tasks_valid_token(valid_token):
    response = get_tasks(valid_token)
    assert_get_all_tasks_success(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion de la lista de tareas es erronea con un token Invalido- SMOKE
def test_get_active_tasks_invalid_token(invalid_token):
    response = get_tasks(invalid_token)
    assert_get_all_tasks_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtnecion filtrada de las tareas por proyecto sea exitosa, con un token valido y un id de proyecto valido - SMOKE
def test_get_tasks_project_valid_token(valid_token, valid_project_id):
    response = get_tasks_from_project(valid_token, valid_project_id)
    assert_get_all_tasks_of_project_success(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion filtrada de las tareas por proyecto, sea erronea con un token Invalido y un id de proyecto valido - SMOKE
def test_get_tasks_project_invalid_token(invalid_token, valid_project_id):
    response = get_tasks_from_project(invalid_token, valid_project_id)
    assert_get_all_tasks_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion filtrada de las tareas por proyecto, sea erronea con un token valido y id de proyecto Invalido e inexistente - SMOKE
def test_get_tasks_project_invalid_id(valid_token, invalid_project_id):
    response = get_tasks_from_project(valid_token, invalid_project_id)
    assert_get_all_tasks_bad_request(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion filtrada de las tareas por seccion, sea exitosa con un token valido, un id de proyecto valido y un id de seccion valido - SMOKE
def test_get_tasks_section_valid_token(valid_token, valid_project_id, valid_id_section):
    response = get_tasks_from_seccion(valid_token, valid_project_id, valid_id_section)
    assert_get_all_tasks_of_seccion_success(response)


@pytest.mark.smoke
@pytest.mark.regression
# TD-13 Verificar si la obtencion filtrada de las tareas por seccion, sea erronea con un token Invalido, un id de proyecto valido y un id de seccion valido - SMOKE
def test_get_tasks_section_invalid_token(invalid_token, valid_project_id, valid_id_section):
    response = get_tasks_from_seccion(invalid_token, valid_project_id, valid_id_section)
    assert_get_all_tasks_unauthorized(response)