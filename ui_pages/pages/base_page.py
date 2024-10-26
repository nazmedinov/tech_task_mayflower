import allure

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from ui_pages.config import PagesURL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui_pages.config import GLOBAL_TIMEOUT_FOR_WAITING, GLOBAL_STEP_FOR_WAITING
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, Optional, Union, Literal


class BasePageLocators(object):
    # xpath of the "Personal Account" button in the page header
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath of the "Login Form Open" button in the page header
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
    # xpath "Accept Cookie" button
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='Принять']")
    # xpath of the "Go To Authorized User Profile" button
    USER_PROFILE_BUTTON = (By.XPATH, "(//span[@class='aside-menu__label'])[1]")


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None
        self.global_timeout = GLOBAL_TIMEOUT_FOR_WAITING
        self.global_step = GLOBAL_STEP_FOR_WAITING

    @allure.step('Opening a page by URL')
    def open_page(self, url: Optional[str] = None):
        """
        Open page using the received url or the default page url.

        :param url: (Optional[str]) The URL of the page to open.
        :return: instance of the class.
        """
        if url is None:
            url = self.current_page_url
        self.browser.get(url)

        return self

    @allure.step('Accepting cookies')
    def accept_cookies(self):
        """
        Wait for the cookie acceptance button to be clickable and clicks it.

        :return: instance of the class.
        """
        try:
            self.wait_and_click(BasePageLocators.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            pass

        return self

    @allure.step('Click on the element without waiting')
    def click(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find the element using the provided locator and click it.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: clicked WebElement.
        """
        try:
            element = self.browser.find_element(*locator)
            element.click()
        except WebDriverException:
            raise WebDriverException(f'Failed to click on the element with locator: {locator}')

        return element

    @allure.step('Click on the element reflected on the page')
    def wait_and_click(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for the element to be visible and then checks if it is clickable before performing the click action.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: clicked WebElement.
        """
        self.wait_for_visibility(locator)
        self.wait_for_element_clickability(locator)
        element = self.click(locator)

        return element

    @allure.step("Deleting a filled value in a text field")
    def clear_field(self, locator: Tuple[str, str]) -> WebElement:
        """
        Clear the value in the specified text field by clicking on it and set its value to an empty string.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement whose value was cleared.
        """
        element = self.wait_and_click(locator)
        self.browser.execute_script("arguments[0].value = '';", element)

        return element

    @allure.step("Filling the value {value} into the text field")
    def set_value_to_field(self, locator: Tuple[str, str], value: str) -> WebElement:
        """
        Set the specified value into the text field by clicking on it and sending the keys.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param value: (str) value to set.
        :return: WebElement where the value was set.
        """
        element = self.wait_and_click(locator)
        element.send_keys(value)

        return element

    @allure.step("Hover over an element")
    def hover_on_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for the element to be visible and then performs a hover action to move the mouse pointer over the element.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement that was hovered over.
        """
        element = self.wait_for_visibility(locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

        return element

    @allure.step("Waiting for an element to appear on the page")
    def wait_for_visibility(self, locator: Tuple[str, str], timeout: int = None, step: int = None) -> WebElement:
        """
        Use WebDriverWait to wait until the element located by the provided locator is visible.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: visible WebElement located by the provided locator.
        """
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} is not visible within {timeout} seconds.")

        return element

    @allure.step("Wait until the element is not visible on the page")
    def wait_for_invisibility(self, locator: Tuple[str, str], timeout: int = None, step: int = None) \
            -> Union[Literal[False, True], WebElement]:
        """
        Use WebDriverWait to wait until the element located by the provided locator is no longer visible.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: WebElement that becomes invisible.
        """
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} did not become invisible within {timeout} seconds.")

        return element

    @allure.step("Waiting for an element to appear in the page's DOM")
    def wait_for_presence(self, locator: Tuple[str, str], timeout: int = None, step: int = None) -> WebElement:
        """
        Use WebDriverWait to check for the presence of an element located by the provided locator.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: WebElement that is present in the DOM.
        """
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} was not found in the DOM within {timeout} seconds.")
        return element

    @allure.step('Wait for the element to be clickable')
    def wait_for_element_clickability(self, locator: Tuple[str, str], timeout: int = None, step: int = None) \
            -> WebElement:
        """
        Use WebDriverWait to check if the element located by the provided locator is clickable.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: The clickable WebElement.
        """
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} is not clickable within {timeout} seconds.")

        return element

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for the element to be present in the DOM and then scrolls the page so that the element.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement that was scrolled into view.
        """
        element = self.wait_for_presence(locator)
        try:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
        except TimeoutException:
            raise AssertionError(f"Failed to scroll to element with locator {locator}.")

        return element

    def check_that_timeout_and_step_filled(self, timeout: Optional[int], step: Optional[int]) -> Tuple[int, int]:
        """
        Ensures that values for timeout and polling step are set. If either is None, assigns default global values.

        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: tuple (timeout, step).
        """
        if timeout is None:
            timeout = self.global_timeout
        if step is None:
            step = self.global_step

        return timeout, step

    @allure.step("Checking that the element is present on the page")
    def is_element_present(self, locator: Tuple[str, str], timeout: int = None, step: int = None) -> bool:
        """
        Wait for the element located by the provided locator to be present in the DOM.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) maximum time in seconds to wait for the condition.
        :param step: (int) interval in seconds to poll the condition.
        :return: True if the element is present, False otherwise.
        """
        timeout, step = self.check_that_timeout_and_step_filled(timeout, step)
        try:
            WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Check if the element text matches the value {text}")
    def is_element_text_correct(self, locator: Tuple[str, str], text: str) -> bool:
        """
        Check if the text of a specified element matches the expected value.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param text: (str) expected text value.
        :return: True if the element's text matches the expected text, False otherwise.
        """
        element = self.wait_for_visibility(locator)

        return element.text == text

    @allure.step("Check if the current url matches the expected {expected_url}")
    def is_current_url_correct(self, expected_url: str) -> bool:
        """
        Check if the current browser URL matches the expected URL.

        :param expected_url: (str) expected url that should be in browser.
        :return: True if the current url matches the expected url, False otherwise.
        """

        return self.browser.current_url == expected_url

    @allure.step('Check that at least one item is present on the page')
    def is_at_least_one_item_present(self, locator: Tuple[str, str]) -> bool:
        """
        Check if at least one instance of the specified element is present on the page.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: True if at least one element is present, False otherwise.
        """

        return len(self.browser.find_elements(*locator)) > 0

    @allure.step('Finds all elements on the page matching the specified locator')
    def find_all_elements(self, locator: Tuple[str, str]) -> list[WebElement]:
        """
        Finds all elements on the page matching the specified locator.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: list of all find WebElements.
        """

        return self.browser.find_elements(*locator)
