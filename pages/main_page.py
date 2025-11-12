from playwright.sync_api import expect
from  pages.hello_page import BasePage


class MainPage(BasePage):
    URL = "https://www.qa-practice.com/"

    def check_welcome_text(self):
        expect(self.page.get_by_text("Hello!")).to_have_text("Hello!")

    def text_input_clickable(self):
        self.page.get_by_role("link", name="Text input").click()
        expect(self.page).to_have_url("https://www.qa-practice.com/elements/input/simple")
        expect(self.page.get_by_role("heading", name="Input field")).to_be_visible()

    def simple_button_clickable(self):
        self.page.get_by_role("link", name="Simple button").click()
        expect(self.page).to_have_url("https://www.qa-practice.com/elements/button/simple")
        expect(self.page.get_by_role("heading", name="Buttons")).to_be_visible()
        expect(self.page.get_by_role("link", name="Simple Button")).to_be_visible()