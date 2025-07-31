import pytest
import requests


@pytest.fixture
def get_users():
    response = requests.get("https://gorest.co.in/public/v1/users")
    return response