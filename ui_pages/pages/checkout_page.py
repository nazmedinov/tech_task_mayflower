import allure

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators


class CheckoutPageLocators(BasePageLocators):
    # xpath of the item in cart list to buy
    ITEM_IN_CART_LIST = (By.XPATH, "//a[@class='cart-checkout-item__title']")
    # xpath of title on cart page
    CHECKOUT_PAGE_TITLE = (By.XPATH, "//div[@class='h1' and text()='Оформление заказа']")
    # xpath of button to remove an item from the list in the cart
    DELETE_ITEM_IN_CART_BUTTON = lambda self, product_name: (By.XPATH, f"//a[@class='cart-checkout-item__title' and "
                                                                       f"text()='{product_name}']/following-sibling::a")


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CHECKOUT_PAGE_URL
        self.checkout_locators = CheckoutPageLocators()

    @allure.step('Check by product name {product_name} that the product is in the cart')
    def is_product_in_cart(self, product_name):
        items_in_cart = [item.text for item in self.find_all_elements(self.checkout_locators.ITEM_IN_CART_LIST)]

        return product_name in items_in_cart

    @allure.step('Delete product from the cart list by name {product_name}')
    def delete_product_from_cart(self, product_name):
        locator = self.checkout_locators.DELETE_ITEM_IN_CART_BUTTON(product_name)
        self.scroll_to_element(locator)
        self.wait_and_click(locator)
        self.wait_for_invisibility(locator)
        # return to cart page in case of redirect from cart page after deleting all items
        if not self.is_current_url_correct(self.url.CHECKOUT_PAGE_URL):
            self.open_page(url=self.url.CHECKOUT_PAGE_URL)
            self.wait_for_visibility(self.checkout_locators.CHECKOUT_PAGE_TITLE)

        return self
