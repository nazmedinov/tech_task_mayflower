import allure
import os

from selenium.webdriver.common.by import By
from ui_pages.pages.base_page import BasePage, BasePageLocators
from dotenv import load_dotenv


class LoginPageLocators(BasePageLocators):
    # xpath of email input field in login form
    LOGIN_FIELD = (By.XPATH, "//input[@name='login']")
    # xpath поля для ввода пароля в форме логина
    PASSWORD_FIELD = (By.XPATH, "//input[@name='pass']")
    # xpath of the password entry field in the login form
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # xpath of the account menu opening button
    ACCOUNT_MENU_BUTTON = (By.XPATH, "//a[@href='/my/']/span[@class='ms-2']")


class LoginPage(BasePage):
    def __init__(self, browser):
        load_dotenv()
        super().__init__(browser)
        self.current_page_url = self.url.MAIN_PAGE_URL
        self.login_locators = LoginPageLocators()

    @allure.step('Opening the login form')
    def open_login_form(self):
        """
        Open the login form from header.

        :return: instance of the class.
        """
        self.wait_and_click(self.login_locators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_and_click(self.login_locators.LOGIN_FORM_BUTTON)

        return self

    @allure.step('Authorization in the login form')
    def login_account_in_form(self):
        """
        Log into account through the login form.

        :return: instance of the class.
        """
        self.clear_field(self.login_locators.LOGIN_FIELD)
        self.set_value_to_field(self.login_locators.LOGIN_FIELD, os.environ.get('LOGIN_EMAIL'))
        self.clear_field(self.login_locators.PASSWORD_FIELD)
        self.set_value_to_field(self.login_locators.PASSWORD_FIELD, os.environ.get('LOGIN_PASSWORD'))
        self.wait_and_click(self.login_locators.LOGIN_BUTTON)

        return self

    @allure.step('Opening the authorized user account menu')
    def open_account_menu(self):
        """
        Open the dropdown menu for the authorized user.

        :return: instance of the class.
        """
        self.wait_and_click(self.login_locators.ACCOUNT_MENU_BUTTON)

        return self
