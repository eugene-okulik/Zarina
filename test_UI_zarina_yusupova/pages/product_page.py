from pages.base_page import BasePage
from pages.locators import product_page_locators as loc
from pages.locators import common_locators as common_loc


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def click_terms_and_conditions_button(self):
        self.find(loc.terms_and_conditions_loc).click()

    def icon_of_facebook_is_displayed(self):
        self.check_element_is_displayed(loc.icon_of_facebook)

    def add_positions_of_product_to_cart(self, number_of_positions):
        for _ in range(number_of_positions - 1):
            self.find(loc.plus_button_loc).click()
        self.find(loc.add_to_cart_button_loc).click()
        self.wait_for_inner_text_is(common_loc.count_of_product_in_cart_loc, number_of_positions)

    def get_product_price(self):
        return self.get_price(loc.product_price_loc)

    def click_selector_of_currency(self):
        self.wait_for_visible(loc.selector_of_currency_loc)
        self.find(loc.selector_of_currency_loc).click()

    def select_eur_currency(self):
        self.find(loc.eur_currency_loc).click()

    def check_that_prices_are_in_euros(self):
        self.wait_for_inner_text_is(loc.price_currency_loc, 'EUR')
