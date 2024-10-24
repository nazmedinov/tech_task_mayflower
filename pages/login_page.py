import allure
import os

from selenium.webdriver.common.by import By
from pages.base_page import BasePage, BasePageLocators
from dotenv import load_dotenv


class LoginPage(BasePage):
    def __init__(self, browser):
        load_dotenv()
        super().__init__(browser)
        self.current_page_url = self.url.MAIN_PAGE_URL
        self.locators = LoginPageLocators()

    @allure.step('Открытие формы логина')
    def open_login_form(self):
        self.wait_and_click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_and_click(self.locators.LOGIN_FORM_BUTTON)

    @allure.step('Авторизация через форму логина')
    def login_account(self):
        self.clear_field(self.locators.LOGIN_FIELD)
        self.set_value_to_field(self.locators.LOGIN_FIELD, os.environ.get('LOGIN_EMAIL'))
        self.clear_field(self.locators.PASSWORD_FIELD)
        self.set_value_to_field(self.locators.PASSWORD_FIELD, os.environ.get('LOGIN_PASSWORD'))
        self.wait_and_click(self.locators.LOGIN_BUTTON)

    @allure.step('Открытие меню аккаунта авторизованного пользователя')
    def open_account_menu(self):
        self.wait_and_click(self.locators.ACCOUNT_MENU_BUTTON)


class LoginPageLocators(BasePageLocators):
    # xpath поля для ввода email в форме логина
    LOGIN_FIELD = (By.XPATH, "//input[@name='login']")
    # xpath поля для ввода пароля в форме логина
    PASSWORD_FIELD = (By.XPATH, "//input[@name='pass']")
    # xpath кнопки "Войти" в аккаунт
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # xpath кнопки открытия меню аккаунта
    ACCOUNT_MENU_BUTTON = (By.XPATH, "//a[@href='/my/']/span[@class='ms-2']")
    # xpath кнопки перехода в профиль авторизованного юзера
    USER_PROFILE_BUTTON = (By.XPATH, "//span[text()='Мой профиль']")
