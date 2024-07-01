import requests
import pytest
from src.postman_requests.tasks.post_update_a_task import update_a_task
from src.login import get_token
from src.assertions.tasks.post_update_a_task_assertions import assert_post_update_a_task_case_one


                    # Test Cases Automatizados:

# 1.- Verificar que se pueda actualizar el titulo de una tarea - Funcional
def test_post_positive1():
  response = update_a_task("8162142610", "{\"content\": \"Tarea 6 actualizar-100\"}", get_token())
  assert_post_update_a_task_case_one(response)


 # 2.- Verificar que se pueda actualizar la descripcion de una tarea - Funcional
def test_post_positive2():
  response = update_a_task("8162142610", "{\"description\": \"actualizando continuamente - 200\"}", get_token())
  assert_post_update_a_task_case_one(response)


# 3.- Verificar que se pueda actualizar la prioridad de una tarea - Funcional Smoke
#@pytest.mark.smoke
def test_post_positive3():
  response = update_a_task("8162142610", "{\"priority\": 1}", get_token())
  assert_post_update_a_task_case_one(response)


# 4.- Verificar que se pueda actualizar las etiquetas de una de una tarea -Funcional
def test_post_positive4():
  response = update_a_task("8162142610", "{\"labels\": [\"automa_00\",\"test850\"]}", get_token())
  assert_post_update_a_task_case_one(response)


# 5.- Verificar que se pueda actualizar la fecha de vencimiento asignada de una tarea - Funcional Smoke
#@pytest.mark.smoke
def test_post_positive5():
  response = update_a_task("8162142610", "{\"due_date\": \"2024-10-29\"}", get_token())
  assert_post_update_a_task_case_one(response)


#6.- Verificar que no pueda actualizar el titulo de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
def test_post_negative1():
  response = update_a_task("8164654097", "{\"content\": \"8*/*98*9\"}", get_token())
  assert_post_update_a_task_case_one(response)

#7.- Verificar que no pueda actualizar la descripcion de una tarea ingresando solamente signos en ves de caracteres alfanumericos - Funcional
def test_post_negative2():
  response = update_a_task("8164654097", "{\"description\": \"//*+6-.'?\"}", get_token())
  assert_post_update_a_task_case_one(response)

#8.- Verificar que no pueda actualizar la fecha de vencimiento de una tarea ingresando una fecha anterior a la fecha actual - Funcional
def test_post_negative3():
  response = update_a_task("8164654097", "{\"due_date\": \"1909-06-30\"}", get_token())
  assert_post_update_a_task_case_one(response)

