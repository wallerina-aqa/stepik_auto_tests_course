from selenium import webdriver
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/selects1.html")

    num1 = int(browser.find_element("css selector", "#num1").text)
    num2 = int(browser.find_element("css selector", "#num2").text)
    value = num1 + num2

    dropdown = Select(browser.find_element("css selector", "#dropdown"))
    dropdown.select_by_value(str(value))

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
