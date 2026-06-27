def test_check_functional_of_terms_and_conditionals_button(product_page):
    product_page.open_page()
    product_page.click_terms_and_conditions_button()
    product_page.check_current_url_is('http://testshop.qa-practice.com/terms')


def test_check_icon_of_facebook_is_displayed(product_page):
    product_page.open_page()
    product_page.icon_of_facebook_is_displayed()


def test_check_that_page_title_is_correct(product_page):
    product_page.open_page()
    product_page.check_title_is('Office Design Software | My Website')


def test_total_price_for_multiple_items_in_cart(product_page, cart_page):
    product_page.open_page()
    product_price = product_page.get_product_price()
    product_page.add_positions_of_product_to_cart(3)
    product_page.header.go_to_cart()
    cart_page.check_that_product_price_is_correct(0, product_price * 3)
