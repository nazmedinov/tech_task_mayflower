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

    @allure.step('Выбор в каталоге категории "Планшеты"')
    def choose_tablets_category(self):
        self.hover_on_element(self.locators.SECTION_ELECTRONIC_BUTTON)
        self.hover_on_element(self.locators.CATEGORY_TABLETS_BUTTON)
        return self


class CatalogPageLocators(BasePageLocators):
    # xpath основной кнопки "Каталог"
    CATALOG_MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'dropdown-catalog-btn')]")
    # xpath кнопки раздела "Электроника" в каталоге
    SECTION_ELECTRONIC_BUTTON = (By.XPATH, "//span[text()='Электроника']")
    # xpath кнопки категории "Планшеты" в каталоге
    CATEGORY_TABLETS_BUTTON = (By.XPATH, "//a[text()='Планшеты' and contains(@class, 'subcat-list-item')]")
    # xpath кнопки планшета DIGMA в каталоге
    DIGMA_TABLET_BUTTON = (By.XPATH, "//div[contains(@class, 'catalog__subsubcat')]//a[text()='Digma']")
    # xpath заголовка на странице планшета DIGMA
    DIGMA_TABLET_TITLE = (By.XPATH, "//main//h1")
    # xpath карточки товара на странице планшетов DIGMA
    DIGMA_TABLET_ITEM = (By.XPATH, "//div[contains(@class, 'item-card__wrapper')]")
