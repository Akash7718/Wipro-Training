from selenium import webdriver
from pages.login_page import LoginPage
import time


driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

# Create Login Page Object
login_page = LoginPage(driver)

# Login and move to Dashboard Page
dashboard_page = login_page.login(
    "Admin",
    "admin123"
)

# Verify Dashboard
text = dashboard_page.get_dashboard_text()

print("Dashboard Heading:", text)

assert text == "Dashboard"

time.sleep(5)

driver.quit()