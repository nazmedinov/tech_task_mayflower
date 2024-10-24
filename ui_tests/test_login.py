import time
import allure

from pages.login_page import LoginPage


@allure.epic('Пользовательские тесты')
class TestLogin:
    @allure.title('Проверка авторизации пользователя с корректными данными')
    def test_login_user(self, browser):
        login_page = LoginPage(browser)
        login_page.open_page()
        login_page.open_login_form()
        login_page.login_account()
        with allure.step('Пользователь успешно залогинен'):
            login_page.open_account_menu()
            assert login_page.browser.find_element(*login_page.locators.USER_PROFILE_BUTTON).text == 'Мой профиль'
