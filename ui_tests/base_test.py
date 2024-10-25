import pytest

from ui_pages.pages.catalog_page import CatalogPage
from ui_pages.pages.checkout_page import CheckoutPage
from ui_pages.pages.login_page import LoginPage
from ui_pages.pages.product_page import ProductPage


class BaseTest(object):
    catalog_page = None
    login_page = None
    checkout_page = None
    product_page = None

    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.catalog_page = CatalogPage(browser)
        self.login_page = LoginPage(browser)
        self.checkout_page = CheckoutPage(browser)
        self.product_page = ProductPage(browser)
