import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_pages.pages.base_page import BasePage


@allure.step('Browser opening')
@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Запуск в headless режиме
    # chrome_options.add_argument('--no-sandbox')  # Отключение песочницы
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--window-size=1920,1080")
    # browser = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=chrome_options)
    chrome_options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
