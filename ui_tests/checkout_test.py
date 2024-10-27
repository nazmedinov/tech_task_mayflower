import allure
import pytest

from data.catalog_main import CatalogMain
from utils.helpers import random_number_in_range


@allure.epic('User tests')
@allure.feature('Shopping Cart')
class TestCheckout:
    @pytest.mark.smoke
    @allure.title('Checking the addition and removal of a tablet product item from the cart')
    def test_add_and_remove_tablet_from_cart(self, catalog_page, product_page, checkout_page):
        catalog_page.open_page()
        catalog_page.select_category_from_main_catalog(CatalogMain.TABLETS)
        catalog_page.open_product_page_by_order_number(random_number_in_range(1, 3))

        product_name = product_page.get_product_name()
        product_page.add_product_to_cart()

        checkout_page.open_page(accept_cookies=False)
        assert checkout_page.is_product_in_cart(product_name), \
            f"The product '{product_name}' should be in the cart, but it was not found."

        checkout_page.delete_product_from_cart(product_name)
        assert not checkout_page.is_product_in_cart(product_name), \
            f"The product '{product_name}' should have been removed from the cart, but it is still present."
