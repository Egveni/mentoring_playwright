from playwright.sync_api import expect
from  pages.hello_page import BasePage
from pages.base_locators import text_input_page_locators

class EmailPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def navigate_to_email_page(self):
        self.page.get_by_role("link", name=text_input_page_locators["text_input"]).click()
        self.page.get_by_role("link", name=text_input_page_locators["email_link"]).click()
        expect(self.page.locator(text_input_page_locators["email_field"])).to_be_visible()


    def check_email_validation_no_error(self, email):
        input_field = self.page.locator(text_input_page_locators["email_field"])
        input_field.type(email)
        input_field.press(text_input_page_locators["enter"])    
        expect(self.page.locator(text_input_page_locators["error_message_email"])).not_to_be_visible()
        expect(self.page.locator(text_input_page_locators["email_placeholder_result"])).to_contain_text(email)


    def check_email_validation_with_error(self, email):
        input_field = self.page.locator(text_input_page_locators["email_field"])
        input_field.type(email)
        input_field.press(text_input_page_locators["enter"])    
        error = self.page.locator(text_input_page_locators["error_message_email"])
        expect(error).to_be_visible()

    def check_email_localhost_no_error(self, email, should_pass):
        input_field = self.page.locator(text_input_page_locators["email_field"])
        input_field.type(email)
        input_field.press(text_input_page_locators["enter"])
        expect(self.page.locator(text_input_page_locators["error_message_email"])).not_to_be_visible()


    def check_email_localhost_error_visible(self, email):
        error = self.page.locator(text_input_page_locators["error_message_email"])
        expect(error).to_be_visible()