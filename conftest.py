import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
@allure.step('Открытие браузера')
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
