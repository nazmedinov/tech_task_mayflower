import allure
import os

from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators
from dotenv import load_dotenv


class CatalogPage(BasePage):
    def __init__(self, browser):
        load_dotenv()
        super().__init__(browser)
        self.current_page_url = self.url.CATALOG_PAGE_URL
        self.locators = CatalogPageLocators()


class CatalogPageLocators(BasePageLocators):
    pass
