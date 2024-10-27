import allure
import os

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class ProductPageLocators(BasePageLocators):
    # xpath of the title of opened item
    OPENED_ITEM_TITLE = (By.XPATH, '//div/h1')
    # xpath of the add to cart button
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='product-controls']//button[contains(@class,'buy')]")


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.PRODUCT_PAGE_URL
        self.product_locators = ProductPageLocators()

    @allure.step('Getting the product name from its page')
    def get_opened_product_name(self) -> str:
        """
        Retrieve the name of the currently opened product.

        :return: (str) the name of the opened product.
        """
        element = self.wait_for_visibility(self.product_locators.OPENED_ITEM_TITLE)

        return element.text

    @allure.step('Add opened product to cart')
    def add_opened_product_to_cart(self):
        """
        Add the currently opened product to the cart.

        :return: instance of the class.
        """
        self.wait_and_click(self.product_locators.ADD_TO_CART_BUTTON)

        return self
