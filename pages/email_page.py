from playwright.sync_api import expect
from  pages.hello_page import BasePage


class EmailPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_email_page(self):
        self.page.get_by_role("link", name="Text input").click()
        self.page.get_by_role("link", name="Email").click()
        expect(self.page.locator("#id_email")).to_be_visible()


    def check_email_validation_no_error(self, email):
        input_field = self.page.locator("#id_email")
        input_field.type(email, delay=100)
        input_field.press("Enter")    
        expect(self.page.locator("#error_1_id_email")).not_to_be_visible()
        expect(self.page.locator("#result")).to_contain_text(email)


    def check_email_validation_with_error(self, email):
        input_field = self.page.locator("#id_email")
        input_field.type(email, delay=100)
        input_field.press("Enter")    
        error = self.page.locator("#error_1_id_email")
        expect(error).to_be_visible()

    def check_email_localhost_no_error(self, email, should_pass):
        input_field = self.page.locator("#id_email")
        input_field.type(email, delay=100)
        input_field.press("Enter")
        expect(self.page.locator("#error_1_id_email")).not_to_be_visible()


    def check_email_localhost_error_visible(self, email):
        error = self.page.locator("#error_1_id_email")
        expect(error).to_be_visible()