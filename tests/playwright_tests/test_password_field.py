import pytest
from playwright.sync_api import Page, expect

def test_user_can_submit_form_by_pressing_enter_text_displayed(page: Page):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    page.click('a[href="/elements/input/passwd"]')
    input_field = page.locator("#id_password")
    input_field.fill("Password1!")
    input_field.press("Enter")
    expect(page.locator("#result")).to_contain_text("Your input was: Password1!")


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
    page.goto("https://www.qa-practice.com")
    page.click('a[href="/elements/input/passwd"]')  
    input_field = page.locator("#id_password")
    input_field.fill(password)
    input_field.press("Enter")
    if should_pass:
        expect(page.locator("#error_1_id_password")).not_to_be_visible()
    else:
        error = page.locator("#error_1_id_password")
        expect(error).to_be_visible()