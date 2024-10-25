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

        self.catalog_page.open_catalog_dropdown().choose_tablets_category()
        self.catalog_page.wait_and_click(self.catalog_page.catalog_locators.DIGMA_TABLET_BUTTON)

        assert self.catalog_page.is_element_text_correct(
            self.catalog_page.catalog_locators.DIGMA_TABLET_TITLE,
            'Digma'
        ), self.catalog_page.error_messages.INCORRECT_ELEMENT_TITLE
        assert self.catalog_page.is_current_url_correct(self.catalog_page.url.DIGMA_TABLET_PAGE_URL), \
            self.catalog_page.error_messages.INCORRECT_URL_PAGE
        assert self.catalog_page.is_at_least_one_item_present(self.catalog_page.catalog_locators.DIGMA_TABLET_ITEM), \
            self.catalog_page.error_messages.INCORRECT_NUMBER_OF_ITEMS
