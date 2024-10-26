import allure
import pytest

from ui_tests.base_test import BaseTest
from data.error_messages import ErrorMessages
from data.catalog_main import CatalogMain
from utils.helpers import random_number_in_range


@allure.epic('User tests')
@allure.feature('Product page')
class TestProduct(BaseTest):
    @pytest.mark.regress
    @allure.title('Checking user can leave a review for product item: tablet ')
    def test_user_leave_review_for_tablet(self):
        self.catalog_page.open_page()
        self.catalog_page.accept_cookies()
        self.catalog_page.select_category_from_main_catalog(CatalogMain.TABLETS)
        self.catalog_page.open_product_page_by_order_number(random_number_in_range(1, 3))
