from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import checkbox_page_locators

class SingleCheckboxPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_single_checkbox_page(self):
        self.page.get_by_role("link", name=checkbox_page_locators["single_checkbox_link"]).click()

    def check_only_one_checkbox_on_page(self):
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).to_be_visible()
        expect(self.page.locator(f'input[type="checkbox"]')).to_have_count(1)
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).to_have_attribute("value", "select me or not")

    def check_user_able_to_select_checkbox(self):
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).to_be_enabled()
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).not_to_be_checked()
        self.page.locator(checkbox_page_locators["single_checkbox"]).click()
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).to_be_checked()

    def check_submit_button_always_enabled(self):
        expect(self.page.locator(checkbox_page_locators["submit_button"])).to_be_enabled()

    def check_submit_button_clickable_when_checkbox_checked(self):
        expect(self.page.locator(checkbox_page_locators["submit_button"])).to_be_enabled()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).not_to_be_visible()
        self.page.locator(checkbox_page_locators["single_checkbox"]).click()
        expect(self.page.locator(checkbox_page_locators["single_checkbox"])).to_be_checked()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).to_contain_text("select me or not")
