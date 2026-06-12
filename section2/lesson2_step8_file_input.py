from pathlib import Path

from faker import Faker
from selenium import webdriver

faker = Faker()

current_file = Path(__file__).resolve()
file_path = current_file.parent / "file.txt"

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/file_input.html")

    first_name_input = browser.find_element("css selector", "[name='firstname']")
    first_name_input.send_keys(faker.first_name())

    last_name_input = browser.find_element("css selector", "[name='lastname']")
    last_name_input.send_keys(faker.last_name())

    email_input = browser.find_element("css selector", "[name='email']")
    email_input.send_keys(faker.email())

    file_input = browser.find_element("css selector", "[name='file']")
    file_input.send_keys(str(file_path))

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
