import time
import pytest
from playwright.sync_api import Page, expect


def test_text_input(page: Page):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    page.get_by_placeholder("Submit me").fill("Hello World")
    time.sleep(5)


@pytest.mark.parametrize("valid_text", [
    "test",
    "Test123",
    "user_name",
    "my-value",
    "Test_123-abc",
    "valid_input-123",
])

def test_valid_inputs(page: Page, valid_text):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()  
    input_field = page.get_by_placeholder("Submit me")
    input_field.fill(valid_text)
    input_field.press("Enter")
    error = page.get_by_text("Enter a valid string consisting of letters, numbers, underscores or hyphens.")
    expect(error).not_to_be_visible()
    time.sleep(2)


@pytest.mark.parametrize("invalid_text,description", [
    ("test@mail"),
    ("hello world"),
    ("тест"),
    ("test!"),
    ("value#123"),
    ("test.com"),
    ("user$name"),
])
def test_invalid_inputs(page: Page, invalid_text, description):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    input_field = page.get_by_placeholder("Submit me")
    input_field.fill(invalid_text)
    input_field.press("Enter")
    error = page.get_by_text("Enter a valid string consisting of letters, numbers, underscores or hyphens.")
    expect(error).to_be_visible()

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
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    input_field = page.get_by_placeholder("Submit me")
    test_text = "a" * length
    input_field.fill(test_text)
    input_field.press("Enter")
    if should_pass:
        expect(page.get_by_text("Please enter 2 or more characters")).not_to_be_visible()
        expect(page.get_by_text("Please enter 25 or fewer characters")).not_to_be_visible()
    else:
        error = page.get_by_text(expected_error)
        expect(error).to_be_visible()


def test_result_appears_after_enter(page: Page):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    input_field = page.get_by_placeholder("Submit me")
    input_field.fill("test")
    input_field.press("Enter")
    expect(page.locator('#result-text')).to_have_text("test")