import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/redirect_accept.html")

    flying_button = browser.find_element("css selector", ".btn")
    flying_button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    number = browser.find_element("css selector", "#input_value").text
    result = calc(number)

    input_field = browser.find_element("css selector", "#answer")
    input_field.send_keys(result)

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
