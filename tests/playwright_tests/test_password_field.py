import pytest
from playwright.sync_api import Page
from pages.password_page import PasswordPage

def test_user_can_submit_form_by_pressing_enter_text_displayed(page: Page):
    password_page = PasswordPage(page)
    password_page.open_page()
    password_page.navigate_to_password_page()
    password_page.check_password_field_working()


@pytest.mark.parametrize("password,should_pass", [
    ("", False),
    ("Pass1!", False),
    ("password1!", False),
    ("PASSWORD1!", False),
    ("PASSWORD1!", False),
    ("Password!", False),
    ("Password1", False),
    ("Password1!", True),
    ("MyPass@123", True),
    ("Test#5678", True),
])
def test_password_validation(page: Page, password, should_pass):
    password_page = PasswordPage(page)
    password_page.open_page()
    password_page.navigate_to_password_page() 
    try:
        password_page.check_password_validation_no_error(password, should_pass)
    except Exception as e:
        password_page.check_password_validation_with_error(password, should_pass)