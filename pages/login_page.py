from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser=browser)
        self.current_page_url = self.url.MAIN_PAGE_URL
