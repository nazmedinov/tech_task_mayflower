import time

import allure
import pytest

from ui_tests.base_test import BaseTest


@allure.epic('User tests')
@allure.feature('Shopping Cart')
class TestCheckout(BaseTest):
    @pytest.mark.smoke
    @allure.title('Checking the addition and removal of a tablet product unit from the cart')
    def test_add_and_remove_digma_from_checkout(self):
        self.catalog_page.open_page(self.checkout_page.url.MAIN_PAGE_URL)
        self.catalog_page.accept_cookies()
        self.catalog_page.open_catalog_dropdown().choose_tablets_category()
        self.catalog_page.wait_and_click(self.catalog_page.catalog_locators.CATEGORY_TABLETS_BUTTON)
        self.catalog_page.open_product_page_by_order_number(3)

        added_item_name = self.product_page.get_the_name_of_the_product()
        # self.product_page.add_open_item_to_cart()

        # self.checkout_page.open_page()
        # list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        #
        # assert added_item_name in list_of_items_in_cart, 'Добавить ассерт фолт'
        #
        # self.checkout_page.delete_last_added_item_from_cart()
        # upd_list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        # assert added_item_name not in upd_list_of_items_in_cart, 'Добавить ассерт фолт'



        # self.checkout_page.open_page(self.checkout_page.url.DIGMA_TABLET_PAGE_URL)
        # self.checkout_page.accept_cookies()
        #
        # added_item_name = self.checkout_page.add_item_to_cart(item_number=1)
        # self.checkout_page.open_page()
        # list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        # assert added_item_name in list_of_items_in_cart, 'Добавить ассерт фолт'
        #
        # self.checkout_page.delete_last_added_item_from_cart()
        # self.checkout_page.open_page()
        # upd_list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        # assert added_item_name not in upd_list_of_items_in_cart, 'Добавить ассерт фолт'
