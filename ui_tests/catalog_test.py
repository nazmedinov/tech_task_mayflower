import allure
import pytest

from data.catalog_dropdown import CatalogDropdown


@allure.epic('User tests')
@allure.feature('Product Catalog')
class TestCatalog:
    @pytest.mark.smoke
    @allure.title('Checking user opening of category through the catalog: Digma tablets')
    def test_open_digma_items_from_catalog(self, catalog_page):
        catalog_page.open_page()
        catalog_page.accept_cookies()

        catalog_page.open_catalog_dropdown()
        catalog_page.hover_on_category_in_dropdown(CatalogDropdown.ELECTRONICS)
        catalog_page.hover_on_category_in_dropdown(CatalogDropdown.ElectronicsGoods.TABLETS)
        catalog_page.click_on_category_in_dropdown(CatalogDropdown.TabletsItems.DIGMA)

        assert catalog_page.is_element_text_correct(catalog_page.catalog_locators.OPENED_CATEGORY_TITLE, 'Digma'), \
            "The title of the opened category should be 'Digma' but it is not."

        assert catalog_page.is_current_url_correct(catalog_page.url.DIGMA_TABLET_PAGE_URL), \
            f"The URL the opened category should be '{catalog_page.url.DIGMA_TABLET_PAGE_URL}' but it is not."

        assert catalog_page.is_at_least_one_item_present(catalog_page.catalog_locators.SINGLE_ITEM_BUTTON), \
            "At least one product must be present in the opened categories, but there are none in the current."
