import allure
import os

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.PRODUCT_PAGE_URL
        self.product_locators = ProductPageLocators()


class ProductPageLocators(BasePageLocators):
    pass
