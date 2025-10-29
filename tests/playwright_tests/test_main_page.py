from playwright.sync_api import Page
from pages.main_page import MainPage


def test_welcome_text(page: Page):
    input_page = MainPage(page)
    input_page.open_base_page()
    input_page.check_welcome_text()


def test_text_input(page: Page):
    input_page = MainPage(page)
    input_page.open_base_page()
    input_page.text_input_clickable()