from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/huge_form.html")

    fields = browser.find_elements("css selector", "input")
    for field in fields:
        field.send_keys("Hello, World!")

    submit_button = browser.find_element("css selector", ".btn")
    submit_button.click()

    alert = browser.switch_to.alert
    code = alert.text.split(":")[1].strip()
    alert.accept()
    print(code)
