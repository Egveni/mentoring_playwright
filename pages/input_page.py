from playwright.sync_api import Playwright, sync_playwright, expect, Page
from  pages.hello_page import BasePage

LINK = "#submit-id-submit"
RESULT = "#id_text_string"


class SimplePage(BasePage):
    URL = "https://www.qa-practice.com/"

    def check_placeholder(self, text):
        link = self.page.locator(LINK)
        link.click()
        result = self.page.locator(RESULT)
        expect(result).to_have_text(text)

    # def click_button(self):
    #     button = self.page.locator(BUTTON)
    #     button.click()


    # def check_result_text_is_(self, text):
    #     result = self.page.locator(RESULT)
    #     expect(result).to_have_text(text)


    # page.goto("https://www.qa-practice.com")
    # page.get_by_role("link", name="Text input").click()
    # input_field = page.get_by_placeholder("Submit me")