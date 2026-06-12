from faker import Faker
from selenium import webdriver

faker = Faker()

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/simple_form_find_task.html")

    first_name_input = browser.find_element("css selector", "[name='first_name']")
    first_name_input.send_keys(faker.first_name())

    last_name_input = browser.find_element("css selector", "[name='last_name']")
    last_name_input.send_keys(faker.last_name())

    city_input = browser.find_element("css selector", ".city")
    city_input.send_keys(faker.city())

    country = browser.find_element("css selector", "#country")
    country.send_keys(faker.country())

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
