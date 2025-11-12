from playwright.sync_api import expect
from  pages.hello_page import BasePage

class SimpleButton(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_simple_button_page(self):
        self.page.get_by_role("link", name="Simple Button").click()

    def check_button_label_visible(self):
        expect(self.page.locator("#submit-id-submit")).to_have_text('Click')

    def check_simple_button_working(self):
        self.page.click("#submit-id-submit")
        expect(self.page.locator("#result-text")).to_have_text("Submitted")