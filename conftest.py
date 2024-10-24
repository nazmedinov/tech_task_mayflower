import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.step('Открытие браузера')
@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
