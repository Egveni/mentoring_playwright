import pytest
from playwright.sync_api import Page, expect
from pages.email_page import EmailPage


# def test_email_validation(page: Page):
#     page.goto("https://www.qa-practice.com")
#     page.get_by_role("link", name="Text input").click()
#     page.get_by_role("link", name="Email field").click()



@pytest.mark.parametrize("email,should_pass", [
    ("invalid", False),
    ("invalid@", False),
    ("@example.com", False),
    ("test@example.com", True),
    ("user.name@example.co.uk", True),
    ("test+tag@example.com", True),
])
def test_email_validation(page: Page, email, should_pass):
    email_page = EmailPage(page)
    email_page.open_page()
    email_page.navigate_to_text_input_page()
    email_page.get_by_role("link", name="Email field").click()
    expect(email_page.locator("#id_email")).to_be_visible()
    input_field = email_page.locator("#id_email")
    input_field.type(email, delay=100)
    input_field.press("Enter")    
    if should_pass:
        expect(email_page.locator("#error_1_id_email")).not_to_be_visible()
        expect(email_page.locator("#result")).to_have_text(f"Your input was: {email}")
    else:
        error = email_page.locator("#error_1_id_email")
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