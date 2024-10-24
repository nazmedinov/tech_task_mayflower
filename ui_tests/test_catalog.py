from pages.catalog_page import CatalogPage


class TestCatalog:
    def test_open_item_in_catalog(self, browser):
        catalog_page = CatalogPage(browser)
        catalog_page.open_page()

