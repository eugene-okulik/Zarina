def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.check_for_empty_cart_message()


def test_title(cart_page):
    cart_page.open_page()
    cart_page.check_title_is('Shopping Cart | My Website')


def test_review_order(cart_page):
    cart_page.open_page()
    cart_page.check_review_order_is_displayed()


def test_add_and_remove_product_from_cart(home_page, cart_page):
    home_page.open_page()
    home_page.add_product_to_cart_by_index()
    home_page.click_continue_shopping_button()
    home_page.header.go_to_cart()
    cart_page.remove_one_position_from_cart()
    cart_page.check_that_count_of_product_in_cart_is(0)
    cart_page.check_for_empty_cart_message()


def test_add_multiple_products_and_update_quantity(home_page, cart_page):
    home_page.open_page()
    home_page.add_product_to_cart_by_index()
    home_page.click_continue_shopping_button()
    home_page.add_product_to_cart_by_index(1)
    home_page.click_continue_shopping_button(2)
    home_page.header.go_to_cart()
    cart_page.add_one_position_to_cart(1)
    cart_page.check_that_value_of_product_is(1, 2)
    cart_page.check_that_value_of_product_is(0, 1)
    cart_page.check_that_count_of_product_in_cart_is(3)


def test_cart_subtotal_calculation_multiple_items(home_page, cart_page):
    home_page.open_page()
    home_page.add_product_to_cart_by_index()
    home_page.click_continue_shopping_button()
    home_page.add_product_to_cart_by_index(1)
    home_page.click_continue_shopping_button(2)
    home_page.header.go_to_cart()
    cart_page.check_that_subtotal_price_in_cart_is_correct()
