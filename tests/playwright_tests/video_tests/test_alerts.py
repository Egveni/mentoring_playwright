from playwright.sync_api import Playwright, sync_playwright, expect, Page

def test_alerts(page: Page):
    page.goto("https://www.demoblaze.com/")
    page.get_by_role(role="link", name="Samsung galaxy s6").click()
    page.get_by_role(role="link", name="Add to cart").click()
    page.wait_for_event("dialog").accept()
    page.locator("#cartur").click()