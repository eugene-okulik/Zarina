import json
import re

from playwright.sync_api import Page, Route, expect


def test_catch_response_2(page: Page):
    new_product_name = 'яблокофон 17 про'

    def handle_route(route: Route):
        response = route.fetch()
        data = response.json()
        data['body']['digitalMat'][0]["familyTypes"][0]['productName'] = new_product_name
        route.fulfill(
            response=response,
            body=json.dumps(data)
        )

    page.route(re.compile('digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-img').nth(0).click()
    header = page.locator('#rf-digitalmat-overlay-label-0').nth(0)
    expect(header).to_have_text(new_product_name)
