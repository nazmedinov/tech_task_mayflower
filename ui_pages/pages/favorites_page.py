import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class FavoritesPageLocators(BasePageLocators):
    # xpath of item in the favorites list
    ITEM_IN_FAVORITES = (By.XPATH, "//a[@class='item-card__title rs-to-product']")
    # xpath of button to remove an item from favorites list
    DELETE_FROM_FAVORITES_BUTTON = lambda self, product_name: \
        (By.XPATH, f"//a[text()='{product_name}']/ancestor::div[2]//a[contains(@class, 'favorite')]")


class FavoritesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.FAVORITES_PAGE_URL
        self.checkout_locators = FavoritesPageLocators()

    @allure.step('Checking product {product_name} is in the favorites list')
    def is_product_in_favorites(self, product_name) -> bool:
        """
        Checking product with specified name is present in the favorites list.

        :param product_name: (str) name of product.
        :return: (bool) True if product is in favorites list, False otherwise.
        """
        items_in_favorites = [item.text for item in self.find_all_elements(self.checkout_locators.ITEM_IN_FAVORITES)]

        return product_name in items_in_favorites

    @allure.step('Delete product {product_name} from the favorites list by its name')
    def delete_product_from_favorites(self, product_name):
        """
        Remove product from the favorites list by its name.

        :param product_name: (str) name of product.
        :return: instance of the class.
        """
        locator = self.checkout_locators.DELETE_FROM_FAVORITES_BUTTON(product_name)
        self.scroll_to_element(locator)
        self.wait_and_click(locator)
        self.wait_for_invisibility(locator)

        return self
