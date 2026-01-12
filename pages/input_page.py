from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import text_input_page_locators

class SimplePage(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_text_input_page(self):
        self.page.get_by_role("link", name=text_input_page_locators["text_input"]).click()

    def check_text_input_page_visibility(self):
        expect(self.page.get_by_role("link", name=text_input_page_locators["text_input"])).to_be_visible()

    def check_text_input_working(self):
        self.page.locator(text_input_page_locators["text_field"]).fill("Hello World")
        expect(self.page.locator(text_input_page_locators["text_field"])).to_have_value("Hello World")
        self.page.wait_for_timeout(5000)

    def check_no_error_visible_for_valid_inputs(self, valid_text):
        input_field = self.page.locator(text_input_page_locators["text_field"])
        input_field.type(valid_text)
        input_field.press(text_input_page_locators["enter"])
        error = self.page.locator(text_input_page_locators["error_message_text"])
        expect(error).not_to_be_visible()

    def check_error_visible_for_invalid_inputs(self, invalid_text):
        input_field = self.page.locator(text_input_page_locators["text_field"])
        input_field.type(invalid_text)
        input_field.press(text_input_page_locators["enter"])
        error = self.page.locator(text_input_page_locators["error_message_text"])
        expect(error).to_be_visible()


    def check_text_length_validation(self, length, should_pass, expected_error):
        input_field = self.page.locator(text_input_page_locators["text_field"])
        test_text = "a" * length
        input_field.type(test_text)
        input_field.press(text_input_page_locators["enter"])
        if should_pass:
            expect(self.page.get_by_text("Please enter 2 or more characters")).not_to_be_visible()
            expect(self.page.get_by_text("Please enter 25 or fewer characters")).not_to_be_visible()
        else:
            error = self.page.get_by_text(expected_error)
            expect(error).to_be_visible()