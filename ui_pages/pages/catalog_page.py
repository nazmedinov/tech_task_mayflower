import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class CatalogPageLocators(BasePageLocators):
    # xpath of the main button "Catalog"
    CATALOG_MENU_BUTTON = (By.XPATH, "//button[contains(@class, 'dropdown-catalog-btn')]")
    # xpath of the button of the section "Electronics" in the catalog
    SECTION_ELECTRONIC_BUTTON = (By.XPATH, "//span[text()='Электроника']")
    # xpath of the "Tablets" category button in the catalog
    CATEGORY_TABLETS_BUTTON = (By.XPATH, "//a[text()='Планшеты' and contains(@class, 'subcat-list-item')]")
    # xpath of DIGMA tablet buttons in the catalog
    DIGMA_TABLET_BUTTON = (By.XPATH, "//div[contains(@class,'catalog__subsubcat')]//a[text()='Digma']")
    # xpath of the header on the DIGMA tablet page
    DIGMA_TABLET_TITLE = (By.XPATH, "//main//h1")
    # xpath of product card on the DIGMA tablets page
    DIGMA_TABLET_ITEM = (By.XPATH, "//div[contains(@class,'item-card__wrapper')]")


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CATALOG_PAGE_URL
        self.catalog_locators = CatalogPageLocators()

    @allure.step('Opening the product catalog')
    def open_catalog_dropdown(self):
        self.wait_and_click(self.catalog_locators.CATALOG_MENU_BUTTON)

        return self

    @allure.step('Select category "Tablets" in the catalog')
    def choose_tablets_category(self):
        self.hover_on_element(self.catalog_locators.SECTION_ELECTRONIC_BUTTON)
        self.hover_on_element(self.catalog_locators.CATEGORY_TABLETS_BUTTON)

        return self
