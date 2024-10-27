import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class ProductPageLocators(BasePageLocators):
    # xpath of the title on opened product page
    OPENED_ITEM_TITLE = (By.XPATH, '//div/h1')
    # xpath of button to add item in cart from opened product page
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='product-controls']//button[contains(@class,'buy')]")
    # xpath of button to add item in favorites from opened product page
    ADD_TO_FAVORITES_BUTTON = (By.XPATH, "//a[@class='product-fav rs-favorite']")


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.PRODUCT_PAGE_URL
        self.product_locators = ProductPageLocators()

    @allure.step('Getting product name from opened product page')
    def get_product_name(self) -> str:
        """
        Retrieve the name of product from opened product page.

        :return: (str) name of product.
        """
        element = self.wait_for_visibility(self.product_locators.OPENED_ITEM_TITLE)

        return element.text

    @allure.step('Add opened product to cart')
    def add_product_to_cart(self):
        """
        Add product to the cart from opened product page.

        :return: instance of the class.
        """
        self.wait_and_click(self.product_locators.ADD_TO_CART_BUTTON)

        return self

    @allure.step('Add opened product to favorites')
    def add_product_to_favorites(self):
        """
        Add product to the favorites from opened product page.

        :return: instance of the class.
        """
        self.scroll_to_element(self.product_locators.ADD_TO_FAVORITES_BUTTON)
        self.wait_and_click(self.product_locators.ADD_TO_FAVORITES_BUTTON)

        return self
