from playwright.sync_api import Page, expect


class BasePage:
    URL = None
    
    def __init__(self, page: Page):
        self.page = page


    def open(self):
        if self.URL:
            self.page.goto(self.URL)
        else:   
            raise NotImplementedError("URL is not defined for this page.")