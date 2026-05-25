from playwright.sync_api import BrowserContext
import pytest
from pages.cart_page import CartPage
from pages.desks_page import DesksPage
from pages.product_page import ProductPage
from pages.home_page import HomePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def desks_page(page):
    return DesksPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def home_page(page):
    return HomePage(page)
