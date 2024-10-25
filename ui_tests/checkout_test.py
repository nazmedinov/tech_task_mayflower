import allure
import pytest

from ui_tests.base_test import BaseTest


@allure.epic('User tests')
@allure.feature('Shopping Cart')
class TestCheckout(BaseTest):
    @pytest.mark.smoke
    @allure.title('Check the addition and removal of a tablet product unit from the cart')
    def test_add_and_remove_tablet_from_cart(self):
        self.catalog_page.open_page()
        self.catalog_page.accept_cookies()
        self.catalog_page.select_category_from_main_catalog(self.catalog_page.catalog_main_items.TABLETS)
        self.catalog_page.open_product_page_by_order_number(1)

        product_name = self.product_page.get_product_name()
        self.product_page.add_opened_item_to_cart()
        self.checkout_page.open_page()
        assert self.checkout_page.is_product_in_cart(product_name), 'Product not found in cart'

        self.checkout_page.delete_product_from_cart_by_name(product_name)
        assert not self.checkout_page.is_product_in_cart(product_name), 'Product should not be in cart'
