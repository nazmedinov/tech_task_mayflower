import allure

from selenium.common import TimeoutException
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

    @allure.step('Click on the element reflected on the page')
    def wait_and_click(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))
        self.wait_for_element_clickability(element)
        self.browser.find_element(*element).click()

        return self

    @allure.step("Deleting a filled value in a text field")
    def clear_field(self, element):
        self.wait_and_click(element)
        input_field = self.browser.find_element(*element)
        self.browser.execute_script("arguments[0].value = '';", input_field)

        return self

    @allure.step("Filling the value {value} into the text field")
    def set_value_to_field(self, element, value):
        self.wait_and_click(element)
        self.browser.find_element(*element).send_keys(value)

        return self

    @allure.step("Hover over an element")
    def hover_on_element(self, element):
        self.wait_for_visibility(element)
        actions = ActionChains(self.browser)
        actions.move_to_element(self.browser.find_element(*element)).perform()

        return self

    @allure.step("Waiting for an element to appear on the page")
    def wait_for_visibility(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(element))

        return self

    @allure.step("Wait until the element is not visible on the page")
    def wait_for_invisibility(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until_not(EC.visibility_of_element_located(element))

        return self

    @allure.step("Waiting for an element to appear in the page's DOM")
    def wait_for_presence(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(element))

        return self

    @allure.step('Wait for the element to be clickable')
    def wait_for_element_clickability(self, element, timeout=None, step=None):
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        WebDriverWait(self.browser, timeout, step).until(EC.element_to_be_clickable(element))

        return self

    @allure.step("Scroll to element")
    def scroll_to_element(self, element):
        self.wait_for_presence(element)
        self.browser.execute_script("arguments[0].scrollIntoView();", self.browser.find_element(*element))

        return self

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
    def is_element_text_correct(self, element, text):
        """
        Check if the text of a specified element matches the expected value.

        Args:
            element (tuple): A locator tuple (By, value) used to find the element.
            text (str): The expected text that should match the element's text.

        Returns:
            bool: True if the element's text matches the expected text, False otherwise.
        """

        return self.wait_for_visibility(element).browser.find_element(*element).text == text

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
    def is_at_least_one_item_present(self, element):
        """
        Check if at least one instance of the specified element is present on the page.

        Args:
            element (tuple): A locator tuple (By, value) used to find the element

        Returns:
            bool: True if at least one element is present, False otherwise.
        """

        return len(self.browser.find_elements(*element)) > 0
