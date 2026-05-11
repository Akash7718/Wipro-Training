from selenium import webdriver
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
# Login
login_page = LoginPage(driver)
login_page.enter_username("Admin")
login_page.enter_password("admin123")
dashboard_page = login_page.click_login()
# Open PIM
pim_page = PIMPage(driver)
pim_page.open_pim()
# View Employee Details
personal_page = pim_page.view_employee_details("Anshu")
# Verification
if personal_page.is_personal_details_displayed():
    print("Personal Details Page Opened")
else:
    print("Failed")
time.sleep(5)
driver.quit()