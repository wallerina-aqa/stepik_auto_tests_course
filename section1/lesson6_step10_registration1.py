from faker import Faker
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

faker = Faker()

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/registration1.html")

    first_name_input = browser.find_element("css selector", ".first_block .first")
    first_name_input.send_keys(faker.first_name())

    last_name_input = browser.find_element("css selector", ".first_block .second")
    last_name_input.send_keys(faker.last_name())

    email_input = browser.find_element("css selector", ".first_block .third")
    email_input.send_keys(faker.email())

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    welcome_message_expected = "Congratulations! You have successfully registered!"

    wait = WebDriverWait(browser, 2)
    welcome_message_actual = wait.until(
        ec.visibility_of_element_located(("css selector", "h1"))
    ).text
    assert welcome_message_actual == welcome_message_expected, (
        f'Should be welcome message "{welcome_message_expected}", '
        f'but got "{welcome_message_actual}"'
    )
