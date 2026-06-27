from playwright.sync_api import Page, expect


class Header:
    def __init__(self, page: Page):
        self.page = page

    def check_logo_is_enabled(self):
        expect(self.page.locator('[aria-label="Main"]  img')).to_be_enabled()

    def go_to_cart(self):
        self.page.locator('[aria-label="Main"] .fa.fa-shopping-cart').click()
