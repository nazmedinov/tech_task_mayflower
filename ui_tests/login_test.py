import allure
import pytest


@allure.epic('User tests')
@allure.feature('User login')
class TestLogin:
    @pytest.mark.smoke
    @allure.title('Checking user authorization with correct data')
    def test_login_user(self, login_page):
        login_page.open_page()
        login_page.accept_cookies()

        login_page.open_login_form().login_account_in_form()
        login_page.open_account_menu()

        assert login_page.is_element_present(login_page.login_locators.USER_PROFILE_BUTTON), \
            "The 'User Profile' button, visible only to authorized users, is not present."

        assert login_page.is_element_text_correct(login_page.login_locators.USER_PROFILE_BUTTON, 'Мой профиль'), \
            "Text on 'User Profile' button, visible only to authorized users, is not correct."
