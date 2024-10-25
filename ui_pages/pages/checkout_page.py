import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class CheckoutPageLocators(BasePageLocators):
    pass


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CHECKOUT_PAGE_URL
        self.locators = CheckoutPageLocators()
