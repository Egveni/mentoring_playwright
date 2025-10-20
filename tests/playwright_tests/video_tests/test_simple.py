from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pages.simple_page import SimplePage


def test_simple(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_exist()


def test_simple_clickable(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.click_button()
    simple_page.check_result_text_is_("Submitted")