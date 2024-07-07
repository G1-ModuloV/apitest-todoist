import pytest
from src.utils.comment import get_all_comments_from_task, get_all_comments_from_project
from src.assertions.comments.get_all_comments_assertions import (assert_get_all_comments_of_task_success,
                                                                 assert_get_all_comments_of_project_success,
                                                                 assert_get_all_comments_bad_request,
                                                                 assert_get_all_comments_not_found,
                                                                 assert_get_all_comments_unauthorized)

@pytest.mark.smoke
# TD-12 Verificar que se obtengan todos los comentarios de una tarea dando un id de tarea válido
def test_get_all_comments_from_task(valid_token, all_comments_valid_task_id):
    response = get_all_comments_from_task(valid_token, all_comments_valid_task_id)
    assert_get_all_comments_of_task_success(response)

@pytest.mark.smoke
# TD-12 Verificar que se obtengan todos los comentarios de un proyecto dando un id de proyecto válido
def test_get_all_comments_from_project(valid_token, all_comments_valid_project_id):
    response = get_all_comments_from_project(valid_token, all_comments_valid_project_id)
    assert_get_all_comments_of_project_success(response)

@pytest.mark.regression
# TD-12 Verificar que se obtenga un error al intentar obtener todos los comentarios de una tarea dando un id de tarea inválido
def test_get_all_comments_from_invalid_task(valid_token, all_comments_invalid_id):
    response = get_all_comments_from_task(valid_token, all_comments_invalid_id)
    assert_get_all_comments_bad_request(response)

@pytest.mark.regression
# TD-12 Verificar que se obtenga un error al intentar obtener todos los comentarios de un proyecto dando un id de proyecto inválido
def test_get_all_comments_from_invalid_project(valid_token, all_comments_invalid_id):
    response = get_all_comments_from_project(valid_token, all_comments_invalid_id)
    assert_get_all_comments_bad_request(response)

@pytest.mark.regression
# TD-12 Verificar que se obtenga un error al intentar obtener todos los comentarios de una tarea dando un id de tarea que fue borrada
def test_get_all_comments_from_deleted_task(valid_token, all_comments_deleted_task_id):
    response = get_all_comments_from_task(valid_token, all_comments_deleted_task_id)
    assert_get_all_comments_not_found(response)

@pytest.mark.regression
# TD-12 Verificar que se obtenga un error al intentar obtener todos los comentarios de un proyecto dando un id de proyecto que fue borrado
def test_get_all_comments_from_deleted_project(valid_token, all_comments_deleted_project_id):
    response = get_all_comments_from_project(valid_token, all_comments_deleted_project_id)
    assert_get_all_comments_not_found(response)

@pytest.mark.regression
# TD-12 Verificar que no se obtegan todos los comentarios de una tarea dando un token de autenticación incorrecto
def test_get_all_comments_from_task_with_invalid_token(invalid_token, all_comments_valid_task_id):
    response = get_all_comments_from_task(invalid_token, all_comments_valid_task_id)
    assert_get_all_comments_unauthorized(response)

@pytest.mark.regression
# TD-12 Verificar que no se obtegan todos los comentarios de una tarea sin dar un token de autenticación
def test_get_all_comments_from_task_without_token(no_token, all_comments_valid_task_id):
    response = get_all_comments_from_task(no_token, all_comments_valid_task_id)
    assert_get_all_comments_unauthorized(response)

@pytest.mark.regression
# TD-12 Verificar que no se obtenga todos los comentarios de un proyecto dando un token de autenticación incorrecto
def test_get_all_comments_from_project_with_invalid_token(invalid_token, all_comments_valid_project_id):
    response = get_all_comments_from_project(invalid_token, all_comments_valid_project_id)
    assert_get_all_comments_unauthorized(response)

@pytest.mark.regression
# TD-12 Verificar que no se obtenga todos los comentarios de un proyecto sin dar un token de autenticación
def test_get_all_comments_from_project_without_token(no_token, all_comments_valid_project_id):
    response = get_all_comments_from_project(no_token, all_comments_valid_project_id)
    assert_get_all_comments_unauthorized(response)
