import allure
import pytest

from data.catalog_main import CatalogMain
from utils.helpers import random_number_in_range


@allure.epic('User tests')
@allure.feature('Product page')
class TestProduct:
    @pytest.mark.regress
    @allure.title('Checking user can leave a review for product item: tablet')
    def test_user_leave_review_for_tablet(self, catalog_page):
        catalog_page.open_page()
        catalog_page.accept_cookies()
        catalog_page.select_category_from_main_catalog(CatalogMain.TABLETS)
        catalog_page.open_product_page_by_order_number(random_number_in_range(1, 3))
