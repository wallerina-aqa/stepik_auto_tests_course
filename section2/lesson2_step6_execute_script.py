import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/execute_script.html")

    number = browser.find_element("css selector", "#input_value").text
    result = calc(number)

    browser.execute_script("window.scrollBy(0, 100)")

    input_field = browser.find_element("css selector", "#answer")
    input_field.send_keys(result)

    robot_checkbox = browser.find_element("css selector", "#robotCheckbox")
    robot_checkbox.click()

    robots_rule_button = browser.find_element("css selector", "#robotsRule")
    robots_rule_button.click()

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
