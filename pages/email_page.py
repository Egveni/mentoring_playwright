from playwright.sync_api import expect
from  pages.hello_page import BasePage


class EmailPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def open_base_page(self):
        self.open_page()

    def navigate_to_text_input_page(self):
        self.page.get_by_role("link", name="Text input").click()