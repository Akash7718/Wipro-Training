from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page2 import AdminPage
import time

# Data Provider
test_users = [
    "Admin",
    "InvalidUser",
    "Paul"
]

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
login_page = LoginPage(driver)

login_page.enter_username("Admin")
login_page.enter_password("admin123")

login_page.click_login()

# Open Admin Page
admin_page = AdminPage(driver)

admin_page.open_admin_page()

# Data Driven Testing
for username in test_users:

    print("\nChecking User:", username)

    if admin_page.is_user_present(username):
        print(username, "Exists")
    else:
        print(username, "Does NOT Exist")

time.sleep(5)

driver.quit()