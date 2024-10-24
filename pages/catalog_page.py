import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CATALOG_PAGE_URL
        self.locators = CatalogPageLocators()

    @allure.step('Открытие каталога товаров')
    def open_catalog_dropdown(self):
        self.wait_and_click(self.locators.CATALOG_MENU_BUTTON)
        return self

    def choose_tablets_category(self):
        self.hover_on_element(self.locators.SECTION_ELECTRONIC_BUTTON)
        return self


class CatalogPageLocators(BasePageLocators):
    # xpath основной кнопки "Каталог"
    CATALOG_MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'dropdown-catalog-btn')]")
    # xpath кнопки раздела "Электроника" в каталоге
    SECTION_ELECTRONIC_BUTTON = (By.XPATH, "//span[text()='Электроника']")
