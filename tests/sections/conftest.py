import pytest
from src.utils.section import post_a_section_and_get_section_id, delete_a_section


@pytest.fixture(scope="session")
def setup_create_a_section(valid_token, valid_project_id, name_section):
    section_id = post_a_section_and_get_section_id(valid_token, valid_project_id, name_section)
    print("Creo una seccion")

    def teardown():
        delete_a_section(valid_token, section_id)

    print("Se elimino la sesion")
    yield section_id
    teardown()


