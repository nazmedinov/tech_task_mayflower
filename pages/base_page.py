import allure

from pages.config import PagesURL


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None

    @allure.step('Открытие страницы по URL адресу')
    def open(self, url=None):
        if url is None:
            url = self.current_page_url
        self.browser.get(url)


class BasePageLocator(object):
    pass
