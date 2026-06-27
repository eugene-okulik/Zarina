from playwright.sync_api import Page, Locator, expect
from pages.header import Header


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page
        self.header = Header(page)

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def get_text(self, locator):
        return self.find(locator).inner_text().strip()

    def clear_text(self, text):
        return text.strip()

    def check_title_is(self, title):
        return expect(self.page).to_have_title(title)

    def check_element_is_displayed(self, locator):
        return self.find(locator).is_visible()

    def clean_price(self, price):
        return float(price.replace(",", "").strip())

    def get_price(self, locator):
        return self.clean_price(self.get_text(locator))

    def wait_for_visible(self, locator, time=10000):
        return expect(self.find(locator)).to_be_visible(timeout=time)

    def wait_for_invisible(self, locator, time=10000):
        return expect(self.find(locator)).not_to_be_visible(timeout=time)

    def check_that_default_state_of_checkboxes_is_unchecked(self, list_of_checkboxes):
        for item in list_of_checkboxes:
            expect(item).not_to_be_checked()

    def check_current_url_is(self, current_url):
        return expect(self.page).to_have_url(current_url)

    def wait_for_inner_text_is(self, locator, text, time=10000):
        return expect(self.find(locator)).to_have_text(str(text), timeout=time)

    def wait_for_current_url_is(self, current_url):
        return expect(self.page).to_have_url(current_url)
