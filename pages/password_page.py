from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import text_input_page_locators

class PasswordPage(BasePage):

    URL = "https://www.qa-practice.com/"

    
    def navigate_to_password_page(self):
        self.page.get_by_role("link", name=text_input_page_locators["text_input"]).click()
        self.page.get_by_role("link", name=text_input_page_locators["password_link"]).click()
        expect(self.page.locator(text_input_page_locators["password_field"])).to_be_visible()


    def check_password_field_working(self):
        input_field = self.page.locator(text_input_page_locators["password_field"])
        input_field.fill("Password1!")  #косяк!!!!!!!!!!!!!!!!
        input_field.press(text_input_page_locators["enter"])
        expect(self.page.locator(text_input_page_locators["text_result"])).to_contain_text("Password1!")


    def check_password_validation_no_error(self, password):
        input_field = self.page.locator(text_input_page_locators["password_field"])
        input_field.fill(password)
        input_field.press(text_input_page_locators["enter"])
        expect(self.page.locator(text_input_page_locators["error_message_password"])).not_to_be_visible()


    def check_password_validation_with_error(self):
        error = self.page.locator(text_input_page_locators["error_message_password"])
        expect(error).to_be_visible()