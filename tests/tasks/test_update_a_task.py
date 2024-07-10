import requests
import pytest
import json
from src.postman_requests.tasks.post_update_a_task import update_a_task
from src.login import get_token
from src.assertions.tasks.update_a_task_assertions import assert_post_update_a_task_case_one
from src.resources.payloads.update_a_task_data import new_content, new_description, new_priority, new_labels, \
    new_due_date, error_content, error_description, error_due_date


@pytest.mark.smoke
@pytest.mark.regresion
# TD-18 Verificar que se pueda actualizar las etiquetas de una de una tarea -Funcional Smoke
def test_post_positive4(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(new_labels), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.smoke
@pytest.mark.regresion
# TD-18 Verificar que no pueda actualizar la fecha de vencimiento de una tarea ingresando una fecha anterior a la fecha actual - Funcional Smoke
def test_post_negative3(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(error_due_date), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que se pueda actualizar el titulo de una tarea - Funcional
def test_post_positive1(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(new_content), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que se pueda actualizar la descripcion de una tarea - Funcional
def test_post_positive2(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(new_description), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que se pueda actualizar la prioridad de una tarea - Funcional
def test_post_positive3(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(new_priority), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que se pueda actualizar la fecha de vencimiento asignada de una tarea - Funcional
def test_post_positive5(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(new_due_date), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que no pueda actualizar el titulo de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
def test_post_negative1(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(error_content), valid_token)
    assert_post_update_a_task_case_one(response)


@pytest.mark.regresion
# TD-18 Verificar que no pueda actualizar la descripcion de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
def test_post_negative2(valid_token, setup_update_task):
    response = update_a_task(setup_update_task, json.dumps(error_description), valid_token)
    assert_post_update_a_task_case_one(response)
