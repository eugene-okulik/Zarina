from playwright.sync_api import Page, expect
import re


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    print('ff')
