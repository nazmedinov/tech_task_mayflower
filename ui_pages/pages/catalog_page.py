import allure

from selenium.webdriver.common.by import By
from data.catalog_categories import CatalogDropdownItems
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
    SINGLE_ITEM_BUTTON = (By.XPATH, "//div[contains(@class,'item-card__wrapper')]")
    # xpath of item in the dropdown catalog
    ITEM_IN_DROPDAWN_CATALOG = lambda self, item_name: (By.XPATH, f"//*[text()='{item_name}'][1]")


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CATALOG_PAGE_URL
        self.catalog_locators = CatalogPageLocators()
        self.catalog_items = CatalogDropdownItems()

    @allure.step('Opening the product catalog')
    def open_catalog_dropdown(self):
        self.wait_and_click(self.catalog_locators.CATALOG_MENU_BUTTON)

        return self

    @allure.step("Hover over an item {item_name} in the dropdown catalog")
    def hover_on_item_in_dropdown(self, item_name):
        locator = self.catalog_locators.ITEM_IN_DROPDAWN_CATALOG(item_name)
        self.hover_on_element(locator)

        return self

    @allure.step("Click on item {item_name} in the dropdown catalog")
    def click_on_item_in_dropdown(self, item_name):
        locator = self.catalog_locators.ITEM_IN_DROPDAWN_CATALOG(item_name)
        self.wait_and_click(locator)

        return self

    # @allure.step('Opening product page from the catalog by product number')
    # def open_product_page_by_order_number(self, item_number=1):
    #     item = self.browser.find_elements(*self.catalog_locators.SINGLE_ITEM_BUTTON)[item_number-1]
    #     self.browser.execute_script("arguments[0].scrollIntoView();", item)
    #     self.wait_for_element_clickability(item)
    #     ActionChains(self.browser).pause(1).click(item).perform()
    #
    #     return self
