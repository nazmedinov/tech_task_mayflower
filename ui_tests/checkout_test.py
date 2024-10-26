import time

import allure
import pytest

from ui_tests.base_test import BaseTest
from data.catalog_main import CatalogMain
from data.error_messages import ErrorMessages
from utils.helpers import random_number_in_range


@allure.epic('User tests')
@allure.feature('Shopping Cart')
class TestCheckout(BaseTest):
    @pytest.mark.smoke
    @allure.title('Checking the addition and removal of a tablet product item from the cart')
    def test_add_and_remove_tablet_from_cart(self):
        self.catalog_page.open_page()
        self.catalog_page.accept_cookies()
        self.catalog_page.select_category_from_main_catalog(CatalogMain.TABLETS)
        self.catalog_page.open_product_page_by_order_number(random_number_in_range(1, 3))

        product_name = self.product_page.get_opened_product_name()
        self.product_page.add_opened_product_to_cart()
        self.checkout_page.open_page()
        assert self.checkout_page.is_product_in_cart(product_name), ErrorMessages.PRODUCT_NOT_FOUND_IN_CART

        self.checkout_page.delete_product_from_cart(product_name)
        assert not self.checkout_page.is_product_in_cart(product_name), ErrorMessages.PRODUCT_SHOULD_NOT_BE_IN_CART
