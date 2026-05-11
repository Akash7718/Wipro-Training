import time
import allure
from pages.login_modal import LoginModal


@allure.feature("Authentication")
@allure.story("Exercise 5: Error Handling & Screenshots")
def test_login_wrong_password_screenshot(driver):
    driver.get("https://www.demoblaze.com/index.html")
    time.sleep(1)

    login = LoginModal(driver)
    login.open_login_modal()
    time.sleep(1)
    login.login("testuser", "wrongpassword123")

    alert_text = login.get_alert_text()

    assert alert_text == "Success", \
        f"Expected 'Success' but got '{alert_text}'"
