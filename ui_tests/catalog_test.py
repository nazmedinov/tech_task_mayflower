import time

import allure
import pytest

from ui_tests.base_test import BaseTest


@allure.epic('User tests')
@allure.feature('Product Catalog')
class TestCatalog(BaseTest):
    @pytest.mark.smoke
    @allure.title('Checking user opening of category through the catalog: Digma tablets')
    def test_open_digma_items_from_catalog(self):
        self.catalog_page.open_page()
        self.catalog_page.accept_cookies()

        self.catalog_page.open_catalog_dropdown()
        self.catalog_page.hover_on_item_in_dropdown(self.catalog_page.catalog_items.ELECTRONICS)
        self.catalog_page.hover_on_item_in_dropdown(self.catalog_page.catalog_items.electronics.TABLETS)
        self.catalog_page.click_on_item_in_dropdown(self.catalog_page.catalog_items.electronics.tablets.DIGMA)

        assert self.catalog_page.is_element_text_correct(
            self.catalog_page.catalog_locators.DIGMA_TABLET_TITLE,
            'Digma'
        ), self.catalog_page.error_messages.INCORRECT_ELEMENT_TITLE

        assert self.catalog_page.is_current_url_correct(self.catalog_page.url.DIGMA_TABLET_PAGE_URL), \
            self.catalog_page.error_messages.INCORRECT_URL_PAGE

        assert self.catalog_page.is_at_least_one_item_present(self.catalog_page.catalog_locators.SINGLE_ITEM_BUTTON), \
            self.catalog_page.error_messages.INCORRECT_NUMBER_OF_ITEMS
