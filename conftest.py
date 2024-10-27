import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ui_pages.pages.login_page import LoginPage
from ui_pages.pages.catalog_page import CatalogPage
from ui_pages.pages.checkout_page import CheckoutPage
from ui_pages.pages.product_page import ProductPage
from ui_pages.pages.favorites_page import FavoritesPage
from data.catalog_main import CatalogMain


@allure.step('Browser opening')
@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--window-size=1920,1080")
    # browser = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', options=chrome_options)
    chrome_options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def catalog_page(browser):
    return CatalogPage(browser)


@pytest.fixture
def product_page(browser):
    return ProductPage(browser)


@pytest.fixture
def checkout_page(browser):
    return CheckoutPage(browser)


@pytest.fixture
def favorites_page(browser):
    return FavoritesPage(browser)


@pytest.fixture
def item_category(request):
    return CatalogMain.CATEGORY_NAMES[request.param]
