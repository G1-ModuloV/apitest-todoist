import requests
import pytest
from src.postman_requests.tasks.post_update_a_task import update_a_task
from src.login import get_token
from src.assertions.tasks.post_update_a_task_assertions import assert_post_update_a_task_case_one

                    # Test Cases Automatizados:

# 1.- Verificar que se pueda actualizar el titulo de una tarea - Funcional
@pytest.mark.regresion
def test_post_positive1(valid_task_id_2, valid_task_payload1):
  response = update_a_task(valid_task_id_2, valid_task_payload1, get_token())
  assert_post_update_a_task_case_one(response)


 # 2.- Verificar que se pueda actualizar la descripcion de una tarea - Funcional
@pytest.mark.regresion
def test_post_positive2(valid_task_id_2, valid_task_payload2):
  response = update_a_task(valid_task_id_2, valid_task_payload2, get_token())
  assert_post_update_a_task_case_one(response)


# 3.- Verificar que se pueda actualizar la prioridad de una tarea - Funcional
@pytest.mark.regresion
def test_post_positive3(valid_task_payload3, valid_task_id_2):
  response = update_a_task(valid_task_id_2, valid_task_payload3, get_token())
  assert_post_update_a_task_case_one(response)


# 4.- Verificar que se pueda actualizar las etiquetas de una de una tarea -Funcional Smoke
@pytest.mark.smoke
def test_post_positive4(valid_task_id_2, valid_task_payload4):
  response = update_a_task(valid_task_id_2, valid_task_payload4, get_token())
  assert_post_update_a_task_case_one(response)


# 5.- Verificar que se pueda actualizar la fecha de vencimiento asignada de una tarea - Funcional
@pytest.mark.regresion
def test_post_positive5(valid_task_id_2, valid_task_payload5):
  response = update_a_task(valid_task_id_2, valid_task_payload5, get_token())
  assert_post_update_a_task_case_one(response)

#6.- Verificar que no pueda actualizar el titulo de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
@pytest.mark.regresion
def test_post_negative1(valid_task_id_3, valid_task_payload6):
  response = update_a_task(valid_task_id_3, valid_task_payload6, get_token())
  assert_post_update_a_task_case_one(response)

#7.- Verificar que no pueda actualizar la descripcion de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
@pytest.mark.regresion
def test_post_negative2(valid_task_payload7, valid_task_id_3):
  response = update_a_task(valid_task_id_3, valid_task_payload7, get_token())
  assert_post_update_a_task_case_one(response)

#8.- Verificar que no pueda actualizar la fecha de vencimiento de una tarea ingresando una fecha anterior a la fecha actual - Funcional Smoke
@pytest.mark.smoke
def test_post_negative3(valid_task_payload8, valid_task_id_3):
  response = update_a_task(valid_task_id_3, valid_task_payload8, get_token())
  assert_post_update_a_task_case_one(response)
