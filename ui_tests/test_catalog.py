import time

import allure

from pages.catalog_page import CatalogPage


@allure.epic('Пользовательские тесты')
class TestCatalog:
    @allure.title('Проверка открытия пользователем товара через каталог: планшет Digma')
    def test_open_digma_in_catalog(self, browser):
        catalog_page = CatalogPage(browser)
        catalog_page.open_page()

        catalog_page.open_catalog_dropdown()
        catalog_page.choose_tablets_category()
        time.sleep(10)
        # catalog_page.wait_and_click()
