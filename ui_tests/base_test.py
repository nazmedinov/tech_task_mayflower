import pytest

from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


class BaseTest(object):
    catalog_page = None
    login_page = None
    checkout_page = None

    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.catalog_page = CatalogPage(browser)
        self.login_page = LoginPage(browser)
        self.checkout_page = CheckoutPage(browser)
