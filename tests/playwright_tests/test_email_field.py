import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("email,should_pass,expected_error", [
    ("invalid", False, "Entered text should be a valid email address"),
    ("invalid@", False, "Entered text should be a valid email address"),
    ("@example.com", False, "Entered text should be a valid email address"),
    ("test@example.com", True, None),
    ("user.name@example.co.uk", True, None),
    ("test+tag@example.com", True, None),
])
def test_email_validation(page: Page, email, should_pass, expected_error):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    page.click('a[href="/elements/input/email"]')
    expect(page.locator('label[for="id_email"]')).to_be_visible()
    input_field = page.locator("#id_email")
    input_field.type(email, delay=100)
    input_field.press("Enter")    
    if should_pass:
        expect(page.locator("#error_1_id_email")).not_to_be_visible()
        expect(page.locator("#result")).to_have_text(f"Your input was: {email}")
    else:
        error = page.locator("#error_1_id_email")
        expect(error).to_be_visible()


@pytest.mark.parametrize("email,should_pass", [
    ("test@localhost", True),
    ("user@localhost", True),
    ("admin@localhost", True),
    ("invalid", False),
    ("test@example.com", True),
])
def test_email_localhost_allowed(page: Page, email, should_pass):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    page.click('a[href="/elements/input/email"]')    
    input_field = page.locator("#id_email")
    input_field.fill(email)
    input_field.press("Enter")
    if should_pass:
        expect(page.locator("#error_1_id_email")).not_to_be_visible()
    else:
        error = page.locator("#error_1_id_email")
        expect(error).to_be_visible()


def test_user_can_submit_form_by_pressing_enter_text_displayed(page: Page):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    page.click('a[href="/elements/input/email"]')
    input_field = page.locator("#id_email")
    input_field.fill("test@example.com")
    input_field.press("Enter")
    expect(page.locator("#result")).to_contain_text("Your input was: test@example.com")