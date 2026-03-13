import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_new_tab(driver):
    driver.implicitly_wait(10)
    driver.get('http://testshop.qa-practice.com/')
    all_images = driver.find_elements(By.CSS_SELECTOR, 'form img')
    name_all_products = driver.find_elements(By.CSS_SELECTOR, '.o_wsale_product_information_text.flex-grow-1 a')
    name_of_product_number_one = name_all_products[0].text
    ActionChains(driver).key_down(Keys.CONTROL).click(all_images[0]).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.CSS_SELECTOR, '#add_to_cart').click()
    driver.find_element(By.CSS_SELECTOR, '.modal-footer button:nth-child(1)').click()
    WebDriverWait(driver, 10).until(lambda d: d.find_element(
        By.CSS_SELECTOR, '[aria-label = "Mobile"] .o_wsale_my_cart sup').get_attribute('innerText') == '1')
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, '[aria-label = "Main"] .o_wsale_my_cart a').click()
    assert name_of_product_number_one in driver.find_element(By.CSS_SELECTOR, '#cart_products .flex-grow-1 a h6').text


def test_pop_up(driver):
    driver.implicitly_wait(5)
    driver.get('http://testshop.qa-practice.com/')
    all_images = driver.find_elements(By.CSS_SELECTOR, 'form img')
    name_all_products = driver.find_elements(By.CSS_SELECTOR, '.o_wsale_product_information_text.flex-grow-1 a')
    name_of_product_number_one = name_all_products[0].text
    ActionChains(driver).move_to_element(all_images[0])
    driver.find_elements(By.CSS_SELECTOR, '[aria-label="Shopping cart"]')[0].click()
    assert name_of_product_number_one in driver.find_element(By.CSS_SELECTOR, '.td-product_name > strong').text
