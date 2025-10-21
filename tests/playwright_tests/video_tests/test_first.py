from playwright.sync_api import Playwright, sync_playwright, expect

def test_wiki(page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("link", name="Русский").click()
    expect(page.get_by_text("Добро пожаловать в Википедию")).to_be_visible()


def test_wiki2(page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role("link", name="Русский").click()
    page.get_by_role("link", name="Содержание").click()
    page.locator("#ca-talk").click()
    expect(page.locator("#firstHeading")).to_have_text("Обсуждение Википедии:Содержание")