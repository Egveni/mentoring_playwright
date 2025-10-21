from playwright.sync_api import Playwright, sync_playwright, expect, Page

def test_iFrame(page: Page):
    page.goto("https://www.qa-practice.com/elements/iframe/iframe_page")
    page.frame_locator("iframe").locator(".navbar-toggler-icon").click()



def test_select(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/select_page")
    page.get_by_role("combobox").select_option("saab")
    expect(page.get_by_role("combobox")).to_have_value("saab")