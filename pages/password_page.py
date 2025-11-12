from playwright.sync_api import expect
from  pages.hello_page import BasePage


class PasswordPage(BasePage):

    URL = "https://www.qa-practice.com/"
    
    def navigate_to_password_page(self):
        self.page.get_by_role("link", name="Text input").click()
        self.page.get_by_role("link", name="Password").click()
        expect(self.page.locator("#id_password")).to_be_visible()


    def check_password_field_working(self):
        input_field = self.page.locator("#id_password")
        input_field.type("Password1!", delay=100)
        input_field.press("Enter")    
        expect(self.page.locator("#result")).to_contain_text("Password1!")


    def check_password_validation_no_error(self, password, should_pass):
        input_field = self.page.locator("#id_password")
        input_field.fill(password)
        input_field.press("Enter")
        expect(self.page.locator("#error_1_id_password")).not_to_be_visible()


    def check_password_validation_with_error(self, password, should_pass):
        error = self.page.locator("#error_1_id_password")
        expect(error).to_be_visible()