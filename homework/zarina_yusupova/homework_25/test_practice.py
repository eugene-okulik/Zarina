import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_input_text(driver):
    input_data = 'Hello_Hello_Hello'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    text_string = driver.find_element(By.NAME, 'text_string')
    text_string.send_keys(input_data)
    text_string.submit()
    result_text = driver.find_element(By.CSS_SELECTOR, '.result-text')
    print(result_text.text)


def test_registration_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Zarina')
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Yusupova')
    email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    email.send_keys('zarina1332484@gmail.com')
    gender = driver.find_element(By.CSS_SELECTOR, '[value="Female"]')
    gender.click()
    number_phone = driver.find_element(By.ID, 'userNumber')
    number_phone.send_keys('9501329565')
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    select_month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    dropdown_month = Select(select_month)
    dropdown_month.select_by_value('0')
    select_year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    dropdown_year = Select(select_year)
    dropdown_year.select_by_value('2000')
    day_of_birth = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--014')
    day_of_birth.click()
    subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subjects.send_keys('M')
    subjects.send_keys(Keys.ENTER)
    second_subject = 'Chemistry'
    subjects.send_keys(second_subject)
    wait = WebDriverWait(driver, 5)
    wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, '.subjects-auto-complete__input-container').get_attribute(
            "data-value") == second_subject
    )
    subjects.send_keys(Keys.ENTER)
    hobbies = driver.find_element(By.CSS_SELECTOR, '#hobbies-checkbox-1')
    hobbies.click()
    current_address = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    current_address.send_keys('Saint-Petersburg, Aviatorov Baltiki 5')
    state = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    state.send_keys('NCR')
    state.send_keys(Keys.ENTER)
    city = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    city.send_keys('Delhi')
    city.send_keys(Keys.ENTER)
    submit_button = driver.find_element(By.CSS_SELECTOR, "#submit")
    submit_button.click()
    final_list = driver.find_elements(By.CSS_SELECTOR, 'tr td')
    result_dict = {}
    for i in range(0, len(final_list), 2):
        key = final_list[i].text
        value = final_list[i + 1].text
        result_dict[key] = value
    print(result_dict)


def test_choose_language(driver):
    input_data = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text(input_data)
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


def test_click_start_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, '#start > button')
    start_button.click()
    finish_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#finish h4'))).text
    assert finish_text == 'Hello World!'
