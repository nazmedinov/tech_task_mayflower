import time

import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators


class CheckoutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.current_page_url = self.url.CHECKOUT_PAGE_URL
        self.locators = CheckoutPageLocators()

    def add_item_to_cart(self, item_number=0):
        item = self.browser.find_elements(*self.locators.ITEM_NAME_INSIDE_CATEGORY)[item_number]
        item_name = item.text
        self.scroll_to_item(item)
        self.wait_until_element_clickable(item)
        ActionChains(self.browser).pause(1).click(item).perform()
        self.wait_for_visibility(self.locators.ADD_TO_CART_BUTTON)
        self.wait_until_element_clickable(self.locators.ADD_TO_CART_BUTTON)
        self.wait_and_click(self.locators.ADD_TO_CART_BUTTON)
        self.browser.back()
        return item_name

    def scroll_to_item(self, item):
        self.browser.execute_script("arguments[0].scrollIntoView();", item)
        return self

    def get_list_of_items_in_cart(self):
        self.wait_for_visibility(self.locators.CART_PAGE_TITLE)
        items = self.browser.find_elements(*self.locators.ITEM_NAME_INSIDE_CART)
        list_of_items_in_cart = []
        if len(items) == 0:
            pass
        else:
            for item in items:
                list_of_items_in_cart.append(item.text)
        return list_of_items_in_cart

    def delete_last_added_item_from_cart(self):
        self.scroll_to_element(self.locators.DELETE_ITEM_FROM_CART_BUTTON)
        self.wait_and_click(self.locators.DELETE_ITEM_FROM_CART_BUTTON)
        return self


class CheckoutPageLocators(BasePageLocators):
    # xpath названия товара внутри выбранной категории
    ITEM_NAME_INSIDE_CATEGORY = (By.XPATH, "//a[contains(@class, 'item-card__title')]")
    # xpath кнопки добавления товара в корзину
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[contains(@class,'order-first')]//span[text()='В корзину']")
    # xpath названия товара внутри корзины
    ITEM_NAME_INSIDE_CART = (By.XPATH, "//a[@class='cart-checkout-item__title']")
    # xpath тайтла на странице корзины товаров
    CART_PAGE_TITLE = (By.XPATH, "//div[text()='Оформление заказа']")
    # xpath кнопки удаления товара из корзины
    DELETE_ITEM_FROM_CART_BUTTON = (By.XPATH, "(//a[contains(@class, 'cart-checkout-item__del')])[last()]")
