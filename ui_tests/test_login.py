from pages.login_page import LoginPage


class TestLogin:
    def test_login_user(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
