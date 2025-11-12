from playwright.sync_api import expect
from  pages.hello_page import BasePage

class DisabledButton(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_disabled_button_page(self):
        self.page.get_by_role("link", name="Simple Button").click()
        self.page.get_by_role("link", name="Disabled").click()

    def check_disabled_button_not_working_by_default(self):
        expect(self.page.locator("#submit-id-submit")).to_be_disabled()

    def enable_disabled_button(self):
        self.page.locator("#id_select_state").click()
        self.page.locator("#id_select_state").select_option("enabled")
        expect(self.page.locator("#submit-id-submit")).to_be_enabled()


    def disable_disabled_button(self):
        self.page.locator("#id_select_state").click()
        self.page.locator("#id_select_state").select_option("disabled")
        expect(self.page.locator("#submit-id-submit")).to_be_disabled()

    def press_submit_button_and_check_success(self):
        self.page.locator("#submit-id-submit").click()
        expect(self.page.locator("#result-text")).to_have_text("Submitted")