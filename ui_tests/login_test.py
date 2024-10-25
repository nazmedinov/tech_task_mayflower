import allure
import pytest

from ui_tests.base_test import BaseTest


@allure.epic('User tests')
@allure.feature('User login')
class TestLogin(BaseTest):
    @pytest.mark.smoke
    @allure.title('Checking user authorization with correct data')
    def test_login_user(self):
        self.login_page.open_page()
        self.login_page.accept_cookies()

        self.login_page.open_login_form().login_account_in_form()
        self.login_page.open_account_menu()

        assert self.login_page.is_element_text_correct(
            self.login_page.login_locators.USER_PROFILE_BUTTON,
            'Мой профиль'
        ), self.login_page.error_messages.INCORRECT_ELEMENT_TEXT
