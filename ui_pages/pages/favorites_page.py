import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class FavoritesPageLocators(BasePageLocators):
    # xpath of the item in favorites list
    ITEM_IN_FAVORITES = (By.XPATH, "//a[@class='item-card__title rs-to-product']")
    # xpath of button to remove an item from favorites list
    DELETE_FROM_FAVORITES_BUTTON = lambda self, product_name: \
        (By.XPATH, f"//a[text()='{product_name}']/ancestor::div[2]//a[contains(@class, 'favorite')]")


class FavoritesPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.FAVORITES_PAGE_URL
        self.checkout_locators = FavoritesPageLocators()

    @allure.step('Check by product name {product_name} that the product is in the favorites list')
    def is_product_in_favorites(self, product_name) -> bool:
        """
        Check if a product with the specified name is present in the favorites list.

        :param product_name: (str) the name of the product.
        :return: (bool) True if the product is in the favorites, False otherwise.
        """
        items_in_favorites = [item.text for item in self.find_all_elements(self.checkout_locators.ITEM_IN_FAVORITES)]

        return product_name in items_in_favorites

    @allure.step('Delete product from the favorites list by name {product_name}')
    def delete_product_from_favorites(self, product_name):
        """
        Remove a product from the favorites by its name.

        :param product_name: (str) the name of the product to be deleted from the favorites.
        :return: instance of the class.
        """
        locator = self.checkout_locators.DELETE_FROM_FAVORITES_BUTTON(product_name)
        self.scroll_to_element(locator)
        self.wait_and_click(locator)
        self.wait_for_invisibility(locator)

        return self
