import time

import allure

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from pages.config import PagesURL, ErrorMessages
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.config import GLOBAL_TIMEOUT_FOR_WAITING, GLOBAL_STEP_FOR_WAITING


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None
        self.global_timeout = GLOBAL_TIMEOUT_FOR_WAITING
        self.global_step = GLOBAL_STEP_FOR_WAITING
        self.error_messages = ErrorMessages()

    @allure.step('Открытие страницы по URL адресу')
    def open_page(self, url=None):
        if url is None:
            url = self.current_page_url
        self.browser.get(url)
        return self

    @allure.step('Принятие куки')
    def accept_cookies(self):
        try:
            self.wait_until_element_clickable(BasePageLocators.COOKIE_ACCEPT_BUTTON)
            self.wait_and_click(BasePageLocators.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            pass

    @allure.step('Клик по появившемуся на странице элементу')
    def wait_and_click(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        self.wait_until_element_clickable(element)
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
        return self

    @allure.step("Проверка на соответствие текста элемента значению {text}")
    def is_element_text_correct(self, element, text):
        self.wait_for_visibility(element)
        return self.browser.find_element(*element).text == text

    @allure.step("Проверка на соответствие текущего url ожидаемому {expected_url}")
    def is_current_url_correct(self, expected_url):
        return self.browser.current_url == expected_url

    @allure.step("Ожидание появления элемента на странице")
    def wait_for_visibility(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        return self

    def wait_for_invisibility(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until_not(EC.visibility_of_element_located(element))
        return self

    # @allure.step("Ожидание появления элемента на странице")
    def wait_for_presence(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(element))
        return self

    @allure.step('Проверяем, что timeout и step для ожиданий определены, либо устанавливаем из глобальных переменных')
    def check_that_timeout_and_step_filled(self, timeout, step):
        if timeout is None:
            timeout = self.global_timeout
        if step is None:
            step = self.global_step
        return timeout, step

    @allure.step('Проверяем, что искомые элементы на странице представлены')
    def verify_elements_present(self, element):
        elements = self.browser.find_elements(*element)
        return len(elements) > 0

    def wait_until_element_clickable(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.element_to_be_clickable(element))
        return self

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        # self.wait_for_visibility(element)
        self.wait_for_presence(element)
        self.browser.execute_script("arguments[0].scrollIntoView();", self.browser.find_element(*element))


class BasePageLocators(object):
    # xpath кнопки "Личный аккаунт" в хедере страницы
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath кнопки "Вход" в хедере страницы для открытия формы логина
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
    # xpath кнопки принятия кук
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='Принять']")
