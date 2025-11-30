from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import checkbox_page_locators

class CheckboxesPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_checkboxes_page(self):
        self.page.get_by_role("link", name=checkbox_page_locators["single_checkbox_link"]).click()
        self.page.get_by_role("link", name=checkbox_page_locators["checkboxes_tab"]).click()

    def check_three_checkboxes_on_page(self):
        expect(self.page.locator(checkbox_page_locators["checkbox_1"])).to_be_visible()
        expect(self.page.locator(checkbox_page_locators["checkbox_2"])).to_be_visible()
        expect(self.page.locator(checkbox_page_locators["checkbox_3"])).to_be_visible()

    def check_labels_of_checkboxes(self):
        expect(self.page.locator(checkbox_page_locators["checkbox_1"])).to_have_attribute("value", "one")
        expect(self.page.locator(checkbox_page_locators["checkbox_2"])).to_have_attribute("value", "two")
        expect(self.page.locator(checkbox_page_locators["checkbox_3"])).to_have_attribute("value", "three")

    def check_user_able_to_select_each_checkbox(self):
        expect(self.page.locator(checkbox_page_locators["checkbox_1"])).not_to_be_checked()
        self.page.locator(checkbox_page_locators["checkbox_1"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_1"])).to_be_checked()
        expect(self.page.locator(checkbox_page_locators["checkbox_2"])).not_to_be_checked()
        self.page.locator(checkbox_page_locators["checkbox_2"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_2"])).to_be_checked()
        expect(self.page.locator(checkbox_page_locators["checkbox_3"])).not_to_be_checked()
        self.page.locator(checkbox_page_locators["checkbox_3"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_3"])).to_be_checked()

    def check_submit_button_always_enabled(self):
        expect(self.page.locator(checkbox_page_locators["submit_button"])).to_be_enabled()

    def check_submit_button_clickable_when_no_checkbox_checked(self):
        expect(self.page.locator(checkbox_page_locators["submit_button"])).to_be_enabled()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).not_to_be_visible()

    def check_submit_button_clickable_when_checkbox_checked_one_by_one(self):
        self.page.locator(checkbox_page_locators["checkbox_1"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_1"])).to_be_checked()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).to_contain_text("one")
        self.page.locator(checkbox_page_locators["checkbox_2"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_2"])).to_be_checked()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).to_contain_text("two")
        self.page.locator(checkbox_page_locators["checkbox_3"]).click()
        expect(self.page.locator(checkbox_page_locators["checkbox_3"])).to_be_checked()
        self.page.locator(checkbox_page_locators["submit_button"]).click()
        expect(self.page.locator(checkbox_page_locators["submit_button_result"])).to_contain_text("three")