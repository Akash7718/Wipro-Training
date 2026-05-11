from selenium import webdriver
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
import time

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
# Use reusable sidebar component
admin_page.side_menu.click_leave()
print("Leave Menu Opened")

time.sleep(5)
driver.quit()