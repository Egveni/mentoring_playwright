

class BasePage:
    URL = None
    
    def __init__(self, page):
        self.page = page


    def open_page(self):
        if self.URL:
            self.page.goto(self.URL)
        else:   
            raise NotImplementedError("URL is not defined for this page.")