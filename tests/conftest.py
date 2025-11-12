import pytest
import requests
import os
from dotenv import load_dotenv
from tools_for_tests import create_booking, delete_booking
from playwright.sync_api import Page
from pages.email_page import EmailPage
from pages.input_page import SimplePage
from pages.looks_like_button_page import LooksLikeButton
from pages.simple_button import SimpleButton
from pages.disabled_page import DisabledButton
from pages.main_page import MainPage
from pages.password_page import PasswordPage
from src.configuration import SERVICE_URL


load_dotenv()

@pytest.fixture(scope="session")
def auth_token():
    auth_url = "https://restful-booker.herokuapp.com/auth"

    username = os.getenv("YOUR_LOGIN")
    password = os.getenv("YOUR_PASSWORD")

    data = {
        "username": f"{username}",
        "password": f"{password}"
    }
    
    auth_response = requests.post(auth_url, json=data)
    
    assert auth_response.status_code == 200, f"Auth failed: {auth_response.status_code}"
    
    token = auth_response.json().get("token")
    
    return token



@pytest.fixture
def create_delete_booking():
    booking_id = create_booking()

    print(f"Booking created with id: {booking_id}")
    yield booking_id

    delete_booking(auth_token, booking_id, SERVICE_URL)
    print(f"\nBooking deleted with id: {booking_id}")



@pytest.fixture(scope="module")
def browser_page(browser):
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


@pytest.fixture
def email_page(browser_page: Page):
    email_page = EmailPage(browser_page)
    yield email_page
    browser_page.context.clear_cookies()

@pytest.fixture
def simple_page(browser_page: Page):
    simple_page = SimplePage(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()

@pytest.fixture
def password_page(browser_page: Page):
    simple_page = PasswordPage(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()

@pytest.fixture
def main_page(browser_page: Page):
    simple_page = MainPage(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()


@pytest.fixture
def simple_button_page(browser_page: Page):
    simple_page = SimpleButton(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()

@pytest.fixture
def looks_like_button_page(browser_page: Page):
    simple_page = LooksLikeButton(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()

@pytest.fixture
def disabled_button_page(browser_page: Page):
    simple_page = DisabledButton(browser_page)
    yield simple_page
    browser_page.context.clear_cookies()