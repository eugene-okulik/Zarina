import re

from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators import cart_page_locators as loc
from pages.locators import common_locators as common_loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    def check_for_empty_cart_message(self):
        expect(self.find(loc.empty_cart_message_loc)).to_have_text('Your cart is empty!')

    def check_review_order_is_displayed(self):
        self.check_element_is_displayed(loc.review_order_loc)

    def remove_one_position_from_cart(self, index=0):
        self.find(loc.list_of_remove_one_button_loc).nth(index).click()

    def add_one_position_to_cart(self, index=0):
        self.find(loc.list_of_add_one_button_loc).nth(index).click()

    def check_that_count_of_product_in_cart_is(self, count):
        self.wait_for_inner_text_is(common_loc.count_of_product_in_cart_loc, count)

    def check_that_value_of_product_is(self, index_of_product, value_of_product):
        product_locator = self.find(loc.list_value_of_product_loc).nth(index_of_product)
        expect(product_locator).to_have_attribute('value', str(value_of_product), timeout=5000)

    def check_that_product_price_is_correct(self, index_of_product, expected_price):
        price_locator = self.find(loc.list_of_product_prices_loc).nth(index_of_product)
        expect(price_locator).to_have_text(re.compile(str(expected_price)))

    def check_that_subtotal_price_in_cart_is_correct(self):
        prices_of_product = [self.clean_price(p.inner_text()) for p in self.find(loc.list_of_product_prices_loc).all()]
        assert sum(prices_of_product) == self.get_price(loc.subtotal_price_loc)
