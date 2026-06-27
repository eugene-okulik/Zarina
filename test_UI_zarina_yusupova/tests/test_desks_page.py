def test_sorting_by_low_to_high(desks_page):
    desks_page.open_page()
    desks_page.select_sorting_by_low_to_high()
    list_of_prices = desks_page.get_item_prices()
    desks_page.check_that_ascending_sorting_is_correct(list_of_prices)


def test_sorting_by_high_to_low(desks_page):
    desks_page.open_page()
    desks_page.select_sorting_by_high_to_low()
    list_of_prices = desks_page.get_item_prices()
    desks_page.check_that_descending_sorting_is_correct(list_of_prices)


def test_sorting_by_name(desks_page):
    desks_page.open_page()
    desks_page.select_sorting_by_name()
    list_of_names = desks_page.get_item_name()
    desks_page.check_that_ascending_sorting_is_correct(list_of_names)


def test_default_state_of_legs_checkboxes(desks_page):
    desks_page.open_page()
    desks_page.check_that_checkboxes_of_legs_are_unchecked()
