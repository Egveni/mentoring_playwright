from playwright.sync_api import Page, expect


def test_welcome_text(page: Page):
    page.goto("https://www.qa-practice.com")
    expect(page.get_by_text("Hello!")).to_have_text("Hello!")


def test_text_input(page: Page):
    page.goto("https://www.qa-practice.com")
    page.get_by_role("link", name="Text input").click()
    expect(page).to_have_url("https://www.qa-practice.com/elements/input/simple")
    expect(page.get_by_role("heading", name="Input field")).to_be_visible()