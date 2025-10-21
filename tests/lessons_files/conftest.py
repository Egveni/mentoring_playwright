import pytest
import requests

from random import randrange
from src.generators.player import Player


@pytest.fixture()
def get_player_generator():
    return Player()

@pytest.fixture()
def get_number():
    return randrange(1, 1000)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    return _calculate

@pytest.fixture()
def make_number():
    print("I'm getting number")
    number = randrange(1, 1000)
    yield
    print(f"I'm done with number {number}")


@pytest.fixture
def get_users():
    response = requests.get("https://gorest.co.in/public/v1/users")
    return response
