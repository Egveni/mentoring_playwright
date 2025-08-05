import requests
import pytest
import allure

from src.baseclasses.response import Response
from src.generators.player_localization import PlayerLocalization

from src.schemas.user import User

from src.schemas.computer import Computer
from computer_json import computer 


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)

@pytest.mark.skip('Skipping issue #1234')
def test_another():
    assert 1 == 1

@pytest.mark.skip('Skipping issue #1234')
def test_another_failing():
    assert 1 == 2

@pytest.mark.production
@pytest.mark.development
@allure.description("Этот тест проверяет форму логина.")
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'c', None),
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result

@allure.tag("smoke")
@allure.tag("regression")
@allure.tag("api")
def test_correct_tags():
    pass


@pytest.mark.parametrize('status', [
    'active',
    'inactive',
     'banned'
])


def test_something1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())

@pytest.mark.parametrize('delete_key', [
    "account status",
    "balance",
    "localize",
    "avatar"
])


def test_something(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)

@pytest.mark.parametrize('localizations', [
    "fr", "de", "ch", "it"
]
)

def test_something2(get_player_generator, localizations):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations], PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


def test_pydentic_object():
    comp = Computer.model_validate(computer)
    print(comp.detailed_info) 
