from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import simple_button_page_locators

class DisabledButton(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_disabled_button_page(self):
        self.page.get_by_role("link", name = simple_button_page_locators["simple_button_link"]).click()
        self.page.get_by_role("link", name = simple_button_page_locators["disabled_button_link"]).click()

    def check_disabled_button_not_working_by_default(self):
        expect(self.page.locator(simple_button_page_locators["click_button_simple_tab"])).to_be_disabled()

    def enable_disabled_button(self):
        self.page.locator(simple_button_page_locators["selector"]).click()
        self.page.locator(simple_button_page_locators["selector"]).select_option("enabled")
        expect(self.page.locator(simple_button_page_locators["click_button_simple_tab"])).to_be_enabled()


    def disable_disabled_button(self):
        self.page.locator(simple_button_page_locators["selector"]).click()
        self.page.locator(simple_button_page_locators["selector"]).select_option("disabled")
        expect(self.page.locator(simple_button_page_locators["click_button_simple_tab"])).to_be_disabled()

    def press_submit_button_and_check_success(self):
        self.page.locator(simple_button_page_locators["click_button_simple_tab"]).click()
        expect(self.page.locator(simple_button_page_locators["submit_result_text"])).to_have_text("Submitted")