import pytest
import requests
from src.login import get_token
from src.utils.task import get_a_task
from src.assertions.tasks.get_an_active_task_assertions import assert_get_a_task, assert_get_a_task_json


# @pytest.mark.smoke
# Verificar que se pueda recuperar una tarea activa con un token de acceso válido
def test_get_an_active_task():
    response = get_a_task("8160389085", get_token())
    assert_get_a_task(response)

# @pytest.mark.smoke
# Verificar que se reciba el contenido de una tarea activa
def test_get_an_active_task_schema():
    response = get_a_task("8160389085", get_token())
    assert_get_a_task_json(response)
