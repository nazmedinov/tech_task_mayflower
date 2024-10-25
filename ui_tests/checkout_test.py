import allure

from ui_tests.base_test import BaseTest


@allure.epic('Пользовательские тесты')
@allure.feature('Корзина товаров')
class TestCheckout(BaseTest):
    @allure.title('Проверка добавления и удаления из корзины единицы товара из категории: планшеты Digma')
    def test_add_and_remove_digma_from_checkout(self):
        self.checkout_page.open_page(self.checkout_page.url.DIGMA_TABLET_PAGE_URL)
        self.checkout_page.accept_cookies()

        added_item_name = self.checkout_page.add_item_to_cart(item_number=0)
        self.checkout_page.open_page()
        list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        assert added_item_name in list_of_items_in_cart

        self.checkout_page.delete_last_added_item_from_cart()
        self.checkout_page.open_page()
        upd_list_of_items_in_cart = self.checkout_page.get_list_of_items_in_cart()
        assert added_item_name not in upd_list_of_items_in_cart
