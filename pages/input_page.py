from playwright.sync_api import expect
from  pages.hello_page import BasePage

class SimplePage(BasePage):
    URL = "https://www.qa-practice.com/"

    def open_base_page(self):
        self.open_page()

    def navigate_to_text_input_page(self):
        self.page.get_by_role("link", name="Text input").click()

        
    def check_text_input_page_visibility(self):
        expect(self.page.get_by_role("link", name="Text input")).to_be_visible()

    def check_text_input_working(self):
        self.page.locator("#id_text_string").fill("Hello World")
        expect(self.page.locator("#id_text_string")).to_have_value("Hello World")
        self.page.wait_for_timeout(5000)

    def check_no_error_visible_for_valid_inputs(self, valid_text):
        input_field = self.page.locator("#id_text_string")
        input_field.type(valid_text, delay=500)
        input_field.press("Enter")
        error = self.page.locator("#error_1_id_text_string")
        expect(error).not_to_be_visible()

    def check_error_visible_for_invalid_inputs(self, invalid_text):
        input_field = self.page.locator("#id_text_string")
        input_field.type(invalid_text, delay=500)
        input_field.press("Enter")
        error = self.page.locator("#error_1_id_text_string")
        expect(error).to_be_visible()


    def check_text_length_validation(self, length, should_pass, expected_error):
        input_field = self.page.locator("#id_text_string")
        test_text = "a" * length
        input_field.type(test_text)
        input_field.press("Enter")
        if should_pass:
            expect(self.page.get_by_text("Please enter 2 or more characters")).not_to_be_visible()
            expect(self.page.get_by_text("Please enter 25 or fewer characters")).not_to_be_visible()
        else:
            error = self.page.get_by_text(expected_error)
            expect(error).to_be_visible()