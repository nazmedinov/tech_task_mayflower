import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class CatalogPageLocators(BasePageLocators):
    # xpath of the main button "Catalog"
    CATALOG_MENU_BUTTON = (By.XPATH, "//button[contains(@class,'dropdown-catalog-btn')]")
    # xpath of the title of opened category
    OPENED_CATEGORY_TITLE = (By.XPATH, "//main//h1")
    # xpath of product card in main catalog
    SINGLE_ITEM_BUTTON = (By.XPATH, "//div[contains(@class,'item-card__wrapper')]")
    # xpath of item in catalog by order number
    ITEM_BY_NUMBER_BUTTON = lambda self, order_number: (By.XPATH, f"(//img[@class='rs-image'])[{order_number}]")
    # xpath of category in the dropdown catalog
    CATEGORY_IN_DROPDAWN_CATALOG = lambda self, category_name: (By.XPATH, f"//*[text()='{category_name}'][1]")
    # xpath of category in the main catalog
    CATEGORY_IN_MAIN_CATALOG = lambda self, category_name: (By.XPATH, f"//div[@class='index-category__title' and "
                                                                      f"text()='{category_name}']")


class CatalogPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CATALOG_PAGE_URL
        self.catalog_locators = CatalogPageLocators()

    @allure.step('Opening the product catalog')
    def open_catalog_dropdown(self):
        self.wait_and_click(self.catalog_locators.CATALOG_MENU_BUTTON)

        return self

    @allure.step("Hover over an category {category_name} in the dropdown catalog")
    def hover_on_item_in_dropdown(self, category_name):
        locator = self.catalog_locators.CATEGORY_IN_DROPDAWN_CATALOG(category_name)
        self.hover_on_element(locator)

        return self

    @allure.step("Click on category {category_name} in the dropdown catalog")
    def click_on_item_in_dropdown(self, category_name):
        locator = self.catalog_locators.CATEGORY_IN_DROPDAWN_CATALOG(category_name)
        self.wait_and_click(locator)

        return self

    @allure.step("Click on category {category_name} from main catalog")
    def select_category_from_main_catalog(self, category_name):
        locator = self.catalog_locators.CATEGORY_IN_MAIN_CATALOG(category_name)
        self.scroll_to_element(locator)
        self.wait_and_click(locator)

        return self

    @allure.step("Open product card in catalog by its number {order_number}")
    def open_product_page_by_order_number(self, order_number):
        locator = self.catalog_locators.ITEM_BY_NUMBER_BUTTON(order_number)
        self.scroll_to_element(locator)
        self.wait_and_click(locator)

        return self
