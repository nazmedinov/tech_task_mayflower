import allure

from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from ui_pages.config import PagesURL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui_pages.config import GLOBAL_TIMEOUT, GLOBAL_STEP
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, Optional, Union, Literal


class BasePageLocators(object):
    # xpath of the "Personal Account" button in the page header
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//span[text()='Личный кабинет']")
    # xpath of the "Login Form Open" button in the page header
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Вход']")
    # xpath "Accept Cookie" button
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='Принять']")
    # xpath of the "My Account" button in the page header for authorized user
    USER_PROFILE_BUTTON = (By.XPATH, "(//span[@class='aside-menu__label'])[1]")


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = PagesURL()
        self.current_page_url = None
        self.global_timeout = GLOBAL_TIMEOUT
        self.global_step = GLOBAL_STEP

    @allure.step('Opening page by URL')
    def open_page(self, url: Optional[str] = None):
        """
        Open page by received or default url.

        :param url: (Optional[str]) page URL.
        :return: instance of the class.
        """
        if url is None:
            url = self.current_page_url
        self.browser.get(url)

        return self

    @allure.step('Accepting cookies')
    def accept_cookies(self):
        """
        Accepting cookies on page.

        :return: instance of the class.
        """
        try:
            self.wait_and_click(BasePageLocators.COOKIE_ACCEPT_BUTTON)
        except (TimeoutException, AssertionError):
            pass

        return self

    @allure.step('Click on the element')
    def click(self, locator: Tuple[str, str]) -> WebElement:
        """
        Click on the element on page.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: clicked WebElement.
        """
        try:
            element = self.browser.find_element(*locator)
            element.click()
        except WebDriverException:
            raise WebDriverException(f'Failed to click on the element with locator: {locator}')

        return element

    @allure.step('Wait for the element and click on it')
    def wait_and_click(self, locator: Tuple[str, str]) -> WebElement:
        """
        Wait for the element and click on it.

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
        Clear the value in text field.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement whose value was cleared.
        """
        element = self.wait_and_click(locator)
        self.browser.execute_script("arguments[0].value = '';", element)

        return element

    @allure.step("Filling the value {value} into the text field")
    def set_value_to_field(self, locator: Tuple[str, str], value: str) -> WebElement:
        """
        Set the specified value into the text field.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param value: (str) value to set.
        :return: WebElement where the value was set.
        """
        element = self.wait_and_click(locator)
        element.send_keys(value)

        return element

    @allure.step("Hover over element")
    def hover_on_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Hover action to move the mouse pointer over the element.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement that was hovered over.
        """
        element = self.wait_for_visibility(locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

        return element

    @allure.step("Waiting for element to appear on page")
    def wait_for_visibility(
            self,
            locator: Tuple[str, str],
            timeout: int = GLOBAL_TIMEOUT,
            step: GLOBAL_STEP = GLOBAL_STEP
    ) -> WebElement:
        """
        Wait until the element is visible.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) time in seconds to wait.
        :param step: (int) interval in seconds to poll.
        :return: visible WebElement.
        """
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} is not visible within {timeout} seconds.")

        return element

    @allure.step("Wait until element is not visible")
    def wait_for_invisibility(self, locator: Tuple[str, str], timeout: int = GLOBAL_TIMEOUT, step: int = GLOBAL_STEP) \
            -> Union[Literal[False, True], WebElement]:
        """
        Wait until element is no longer visible.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) time in seconds to wait.
        :param step: (int) interval in seconds to poll.
        :return: invisible WebElement.
        """
        try:
            element = WebDriverWait(self.browser, timeout, step).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} did not become invisible within {timeout} seconds.")

        return element

    @allure.step("Waiting for element to appear in page's DOM")
    def wait_for_presence(self, locator: Tuple[str, str], timeout: int = GLOBAL_TIMEOUT, step: int = GLOBAL_STEP) \
            -> WebElement:
        """
        Wait for the presence of element in DOM.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) time in seconds to wait.
        :param step: (int) interval in seconds to poll.
        :return: presented in the DOM WebElement.
        """
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} was not found in the DOM within {timeout} seconds.")
        return element

    @allure.step('Wait for element to be clickable')
    def wait_for_element_clickability(
            self,
            locator: Tuple[str, str],
            timeout: int = GLOBAL_TIMEOUT,
            step: int = GLOBAL_STEP
    ) -> WebElement:
        """
        Wait until element is clickable.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) time in seconds to wait.
        :param step: (int) interval in seconds to poll.
        :return: clickable WebElement.
        """
        try:
            element = WebDriverWait(self.browser, timeout, step).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} is not clickable within {timeout} seconds.")

        return element

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Scroll the page to element.

        :param locator: (Tuple[str, str]) tuple with locator.
        :return: WebElement that was scrolled into view.
        """
        element = self.wait_for_presence(locator)
        try:
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
        except TimeoutException:
            raise AssertionError(f"Failed to scroll to element with locator {locator}.")

        return element

    @allure.step("Checking that element is present on the page")
    def is_element_present(
            self,
            locator: Tuple[str, str],
            timeout: int = GLOBAL_TIMEOUT,
            step: int = GLOBAL_STEP
    ) -> bool:
        """
        Check if the element is in the DOM.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param timeout: (int) time in seconds to wait.
        :param step: (int) interval in seconds to poll.
        :return: True if the element is present, False otherwise.
        """
        try:
            WebDriverWait(self.browser, timeout, step).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    @allure.step("Check if the element text matches the value {text}")
    def is_element_text_correct(self, locator: Tuple[str, str], text: str) -> bool:
        """
        Check if the text of element matches the expected value.

        :param locator: (Tuple[str, str]) tuple with locator.
        :param text: (str) expected text value.
        :return: True if element's text matches the expected text, False otherwise.
        """
        element = self.wait_for_visibility(locator)

        return element.text == text

    @allure.step("Check if the current url matches the expected {expected_url}")
    def is_current_url_correct(self, expected_url: str) -> bool:
        """
        Check if the current URL matches the expected URL.

        :param expected_url: (str) expected url.
        :return: True if the current url matches the expected url, False otherwise.
        """

        return self.browser.current_url == expected_url

    @allure.step('Check that at least one item is present on the page')
    def is_at_least_one_item_present(self, locator: Tuple[str, str]) -> bool:
        """
        Check if at least one of the specified elements is on the page.

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
