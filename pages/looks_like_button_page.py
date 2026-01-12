from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import simple_button_page_locators

class LooksLikeButton(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_looks_like_button_page(self):
        self.page.get_by_role("link", name="Simple Button").click()
        self.page.get_by_role("link", name="Looks like a Button").click()

    def check_button_label_visible(self):
        expect(self.page.locator(simple_button_page_locators["click_button_looks_like_tab"])).to_have_text('Click')

    def check_looks_like_button_working(self):
        self.page.locator(simple_button_page_locators["click_button_looks_like_tab"]).click()
        self.page.wait_for_selector("#result-text", timeout=5000)
        expect(self.page.locator(simple_button_page_locators["submit_result_text"])).to_have_text("Submitted")