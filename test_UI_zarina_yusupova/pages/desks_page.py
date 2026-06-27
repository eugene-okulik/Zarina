from pages.base_page import BasePage
from pages.locators import desks_page_locators as loc


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    def sort_by_button_click(self):
        self.find(loc.sort_by_loc).click()

    def select_sorting_by_low_to_high(self):
        self.sort_by_button_click()
        self.find(loc.sort_by_low_to_high_loc).click()

    def select_sorting_by_high_to_low(self):
        self.sort_by_button_click()
        self.find(loc.sort_by_high_to_low_loc).click()

    def select_sorting_by_name(self):
        self.sort_by_button_click()
        self.find(loc.sort_by_name_loc).click()

    def get_item_prices(self):
        prices = [self.clean_price(p.inner_text()) for p in self.find(loc.list_of_prices_loc).all()]
        return prices

    def get_item_name(self):
        names = [self.clear_text(n.inner_text()) for n in self.find(loc.list_of_names_loc).all()]
        return names

    def check_that_ascending_sorting_is_correct(self, list_of_items):
        assert list_of_items == sorted(list_of_items)

    def check_that_descending_sorting_is_correct(self, list_of_items):
        assert list_of_items == sorted(list_of_items, reverse=True)

    def list_of_checkboxes(self):
        return self.find(loc.list_of_checkboxes_loc).all()

    def check_that_checkboxes_of_legs_are_unchecked(self):
        self.check_that_default_state_of_checkboxes_is_unchecked(self.list_of_checkboxes())
