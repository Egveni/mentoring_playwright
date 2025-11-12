from playwright.sync_api import expect
from  pages.hello_page import BasePage

class LooksLikeButton(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_looks_like_button_page(self):
        self.page.get_by_role("link", name="Simple Button").click()
        self.page.get_by_role("link", name="Looks like a Button").click()

    def check_button_label_visible(self):
        expect(self.page.locator("#button-form")).to_have_text('Click')

    def check_looks_like_button_working(self):
        self.page.locator(".a-button").click()
        expect(self.page.locator("#result-text")).to_have_text("Submitted")