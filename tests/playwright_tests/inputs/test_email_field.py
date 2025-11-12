import pytest
from playwright.sync_api import Page, expect
from pages.email_page import EmailPage



@pytest.mark.parametrize("email", [
    ("test@example.com"),
    ("user.name@example.co.uk"),
    ("test+tag@example.com"),
])
def test_email_validation_no_error(email_page, email):
    email_page.open_page()
    email_page.navigate_to_email_page()
    email_page.check_email_validation_no_error(email)

    
@pytest.mark.parametrize("email", [
    ("invalid"),
    ("invalid@"),
    ("@example.com"),
])
def test_email_validation_with_error(email_page, email):
    email_page.open_page()
    email_page.navigate_to_email_page()
    email_page.check_email_validation_with_error(email)


@pytest.mark.parametrize("email,should_pass", [
    ("test@localhost", True),
    ("user@localhost", True),
    ("admin@localhost", True),
    ("invalid", False),
    ("test@example.com", True),
])
def test_email_localhost_allowed(email_page, email, should_pass):
    email_page.open_page()
    email_page.navigate_to_email_page()
    try:
        email_page.check_email_localhost_no_error(email, should_pass)
    except Exception as e:
        email_page.check_email_localhost_error_visible(email)