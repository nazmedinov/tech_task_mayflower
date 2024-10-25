import allure

from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from ui_pages.config import PagesURL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui_pages.config import GLOBAL_TIMEOUT_FOR_WAITING, GLOBAL_STEP_FOR_WAITING
from ui_pages.error_messages import ErrorMessages


class BasePageLocators(object):
    # xpath of the "Personal Account" button in the page header
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath of the "Login Form Open" button in the page header
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
    # xpath "Accept Cookie" button
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='Принять']")
    # xpath of the "Go To Authorized User Profile" button
    USER_PROFILE_BUTTON = (By.XPATH, "//span[text()='Мой профиль']")


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None
        self.global_timeout = GLOBAL_TIMEOUT_FOR_WAITING
        self.global_step = GLOBAL_STEP_FOR_WAITING
        self.error_messages = ErrorMessages()

    @allure.step('Opening a page by URL')
    def open_page(self, url=None):
        if url is None:
            url = self.current_page_url
        self.browser.get(url)

        return self

    @allure.step('Accepting cookies')
    def accept_cookies(self):
        try:
            self.wait_and_click(BasePageLocators.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            pass

        return self

    @allure.step('Click on the element without waiting')
    def click(self, locator):
        try:
            element = self.browser.find_element(*locator)
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            raise ElementClickInterceptedException(self.error_messages.ELEMENT_FAILED_CLICK)

        return element

    @allure.step('Click on the element reflected on the page')
    def wait_and_click(self, locator):
        self.wait_for_visibility(locator)
        self.wait_for_element_clickability(locator)
        element = self.click(locator)

        return element

    @allure.step("Deleting a filled value in a text field")
    def clear_field(self, locator):
        element = self.wait_and_click(locator)
        self.browser.execute_script("arguments[0].value = '';", element)

        return element

    @allure.step("Filling the value {value} into the text field")
    def set_value_to_field(self, locator, value):
        element = self.wait_and_click(locator)
        element.send_keys(value)

        return element

    @allure.step("Hover over an element")
    def hover_on_element(self, locator):
        element = self.wait_for_visibility(locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

        return element

    @allure.step("Waiting for an element to appear on the page")
    def wait_for_visibility(self, locator, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(self.error_messages.ELEMENT_NOT_VISIBLE)

        return element

    @allure.step("Wait until the element is not visible on the page")
    def wait_for_invisibility(self, locator, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(self.error_messages.ELEMENT_NOT_INVISIBLE)
        return element

    @allure.step("Waiting for an element to appear in the page's DOM")
    def wait_for_presence(self, locator, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(self.error_messages.ELEMENT_NOT_PRESENT)
        return element

    @allure.step('Wait for the element to be clickable')
    def wait_for_element_clickability(self, locator, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(self.error_messages.ELEMENT_NOT_CLICKABLE)

        return element

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        element = self.wait_for_presence(locator)
        try:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
        except TimeoutException:
            raise AssertionError(self.error_messages.ELEMENT_FAILED_SCROLL)

        return element

    def check_that_timeout_and_step_filled(self, timeout, step):
        """
        Ensures that values for timeout and polling step are set. If either is None,
        assigns default global values.

        Args:
            timeout (int or None)
            step (int or None)

        Returns:
            tuple: A tuple (timeout, step) with the final values for timeout and polling interval.
        """
        if timeout is None:
            timeout = self.global_timeout
        if step is None:
            step = self.global_step

        return timeout, step

    @allure.step("Check if the element text matches the value {text}")
    def is_element_text_correct(self, locator, text):
        """
        Check if the text of a specified element matches the expected value.

        Args:
            locator (tuple): A locator tuple (By, value) used to find the element.
            text (str): The expected text that should match the element's text.

        Returns:
            bool: True if the element's text matches the expected text, False otherwise.
        """
        element = self.wait_for_visibility(locator)

        return element.text == text

    @allure.step("Check if the current url matches the expected {expected_url}")
    def is_current_url_correct(self, expected_url):
        """
        Check if the current browser URL matches the expected URL.

        Args:
            expected_url (str): The expected URL that the browser should be at.

        Returns:
            bool: True if the current URL matches the expected URL, False otherwise.
        """

        return self.browser.current_url == expected_url

    @allure.step('Check that at least one item is present on the page')
    def is_at_least_one_item_present(self, locator):
        """
        Check if at least one instance of the specified element is present on the page.

        Args:
            locator (tuple): A locator tuple (By, value) used to find the element.

        Returns:
            bool: True if at least one element is present, False otherwise.
        """

        return len(self.browser.find_elements(*locator)) > 0
