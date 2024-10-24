import allure

from pages.config import PagesURL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None
        self.global_timeout = 30
        self.global_step = 3

    @allure.step('Открытие страницы по URL адресу')
    def open_page(self, url=None):
        if url is None:
            url = self.current_page_url
        self.browser.get(url)

    @allure.step('Клик по появившемуся на странице элементу')
    def wait_and_click(self, element, timeout=None, step=None):
        if timeout is None:
            timeout = self.global_timeout
        if step is None:
            step = self.global_step
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        self.browser.find_element(*element).click()

    @allure.step("Удаление заполненного значения в текстовом поле")
    def clear_field(self, element):
        self.wait_and_click(element)
        input_field = self.browser.find_element(*element)
        self.browser.execute_script("arguments[0].value = '';", input_field)

    @allure.step("Заполнение значения {value} в текстовое поле")
    def set_value_to_field(self, element, value):
        self.wait_and_click(element)
        self.browser.find_element(*element).send_keys(value)


class BasePageLocators(object):
    # xpath кнопки "Личный аккаунт" в хедере страницы
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath кнопки "Вход" в хедере страницы для открытия формы логина
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
