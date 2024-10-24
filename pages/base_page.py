import allure

from selenium.webdriver import ActionChains
from pages.config import PagesURL, ErrorMessages
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
        self.error_messages = ErrorMessages()

    @allure.step('Открытие страницы по URL адресу')
    def open_page(self, url=None):
        if url is None:
            url = self.current_page_url
        self.browser.get(url)
        return self

    @allure.step('Клик по появившемуся на странице элементу')
    def wait_and_click(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        self.browser.find_element(*element).click()
        return self

    @allure.step("Удаление заполненного значения в текстовом поле")
    def clear_field(self, element):
        self.wait_and_click(element)
        input_field = self.browser.find_element(*element)
        self.browser.execute_script("arguments[0].value = '';", input_field)
        return self

    @allure.step("Заполнение значения {value} в текстовое поле")
    def set_value_to_field(self, element, value):
        self.wait_and_click(element)
        self.browser.find_element(*element).send_keys(value)
        return self

    @allure.step("Наведение курсора на элемент")
    def hover_on_element(self, element):
        self.wait_for_visibility(element)
        actions = ActionChains(self.browser)
        actions.move_to_element(self.browser.find_element(*element)).perform()

    @allure.step("Проверка на соответствие текста элемента значению {text}")
    def is_element_text_correct(self, element, text):
        return self.browser.find_element(*element).text == text

    @allure.step("Ожидание появления элемента на странице")
    def wait_for_visibility(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        return self

    @allure.step('Проверяем, что timeout и step для ожиданий определены, либо устанавливаем из глобальных переменных')
    def check_that_timeout_and_step_filled(self, timeout, step):
        if timeout is None:
            timeout = self.global_timeout
        if step is None:
            step = self.global_step
        return timeout, step


class BasePageLocators(object):
    # xpath кнопки "Личный аккаунт" в хедере страницы
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath кнопки "Вход" в хедере страницы для открытия формы логина
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
