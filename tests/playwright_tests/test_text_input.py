import pytest
from playwright.sync_api import Page, expect
from pages.input_page import SimplePage


def test_text_input(page: Page):
    input_page = SimplePage(page)
    input_page.open_page()
    input_page.check_text_input_page_visibility()
    input_page.navigate_to_text_input_page()
    input_page.check_text_input_working()

@pytest.mark.parametrize("valid_text", [
    "test",
    "Test123",
    "user_name",
    "my-value",
    "Test_123-abc",
    "valid_input-123",
])

def test_valid_inputs(page: Page, valid_text):
    input_page = SimplePage(page)
    input_page.open_page()
    input_page.check_text_input_page_visibility()
    input_page.navigate_to_text_input_page()
    input_page.check_no_error_visible_for_valid_inputs(valid_text)

@pytest.mark.parametrize("invalid_text", [
    ("test@mail"),
    ("hello world"),
    ("тест"),
    ("test!"),
    ("value#123"),
    ("test.com"),
    ("user$name"),
])
def test_invalid_inputs(page: Page, invalid_text):
    input_page = SimplePage(page)
    input_page.open_page()
    input_page.navigate_to_text_input_page()
    input_page.check_error_visible_for_invalid_inputs(invalid_text)

@pytest.mark.parametrize("length,should_pass,expected_error", [
    (1, False, "Please enter 2 or more characters"),  
    (2, True, None),
    (3, True, None),
    (10, True, None),
    (24, True, None),
    (25, True, None),
    (26, False, "Please enter no more than 25 characters"),
    (30, False, "Please enter no more than 25 characters"),
])
def test_text_length_validation(page: Page, length, should_pass, expected_error):
    input_page = SimplePage(page)
    input_page.open_page()
    input_page.navigate_to_text_input_page()
    input_page.check_text_length_validation(length, should_pass, expected_error)