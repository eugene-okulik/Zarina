def test_logo_of_website(cart_page):
    cart_page.open_page()
    cart_page.header.check_logo_is_enabled()
