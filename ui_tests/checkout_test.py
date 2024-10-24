import time

import allure

from ui_tests.base_test import BaseTest


@allure.epic('Пользовательские тесты')
@allure.feature('Корзина товаров')
class TestCheckout(BaseTest):
    @allure.title('Проверка добавления и удаления из корзины единицы товара: планшет Digma')
    def test_add_and_remove_digma_from_checkout(self):
        self.checkout_page.open_page(self.checkout_page.url.DIGMA_TABLET_PAGE_URL)
        self.checkout_page.accept_cookies()
        time.sleep(10)
