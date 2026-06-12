import math

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    wait = WebDriverWait(browser, 15)
    price_locator = ("css selector", "#price")
    wait.until(ec.text_to_be_present_in_element(price_locator, "100"))

    book_button = browser.find_element("css selector", "#book")
    book_button.click()

    number = browser.find_element("css selector", "#input_value").text
    result = calc(number)

    input_field = browser.find_element("css selector", "#answer")
    input_field.send_keys(result)

    submit_button = browser.find_element("css selector", "#solve")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
