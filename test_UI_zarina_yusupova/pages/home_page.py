from pages.base_page import BasePage
from pages.locators import home_page_locators as loc
from selenium.webdriver import ActionChains


class HomePage(BasePage):
    page_url = '/shop'

    def click_first_image_of_product(self):
        self.find(loc.list_of_images_loc).nth(0).click()

    def click_continue_shopping_button(self, expected_count=1):
        self.find(loc.continue_shopping_button_loc).click()
        self.wait_for_inner_text_is(loc.count_of_product_in_cart_loc, expected_count)

    def add_product_to_cart_by_index(self, index=0):
        self.find(loc.list_of_images_loc).nth(index).hover()
        self.find(loc.list_of_icon_of_cart_loc).nth(index).click()
