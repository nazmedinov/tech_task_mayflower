import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CHECKOUT_PAGE_URL
        self.locators = CheckoutPageLocators()


class CheckoutPageLocators(BasePageLocators):
    pass
