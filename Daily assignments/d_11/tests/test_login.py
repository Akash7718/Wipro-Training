from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Create object of LoginPage
login_page = LoginPage(driver)

# Call methods
login_page.login("Admin", "admin123")
time.sleep(5)
driver.quit()