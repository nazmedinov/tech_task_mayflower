import time

import allure
import pytest

from utils.helpers import random_number_in_range


@allure.epic('User tests')
@allure.feature('Product Page')
class TestProduct:
    @pytest.mark.regress
    @pytest.mark.parametrize('item_category',
                             [pytest.param('tablets', id='product from tablets'),
                              pytest.param('laptops', id='product from laptops'),
                              pytest.param('phones', id='product from phones')], indirect=True)
    @allure.title('Checking the addition and removal opened item from favorites')
    def test_add_and_remove_item_from_favorites(self, catalog_page, product_page, favorites_page, item_category):
        catalog_page.open_page()
        catalog_page.accept_cookies()
        catalog_page.select_category_from_main_catalog(item_category)
        catalog_page.open_product_page_by_order_number(random_number_in_range(1, 3))

        product_name = product_page.get_product_name()
        product_page.add_product_to_favorites()

        favorites_page.open_page()
        assert favorites_page.is_product_in_favorites(product_name), \
            f"The product '{product_name}' should be in the favorites list, but it was not found."

        favorites_page.delete_product_from_favorites(product_name)
        assert not favorites_page.is_product_in_favorites(product_name), \
            f"The product '{product_name}' should have been removed from favorites list, but it is still present."
