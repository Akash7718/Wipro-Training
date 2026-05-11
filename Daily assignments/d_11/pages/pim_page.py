from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.personal_details_page import PersonalDetailsPage


class PIMPage:

    def __init__(self, driver):
        self.driver = driver

        self.pim_menu = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span']")

        self.employee_name_input = (
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
        )

        self.search_button = (
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
        )

    def open_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def view_employee_details(self, employee_name):
        # Enter employee name
        self.driver.find_element(*self.employee_name_input).send_keys(employee_name)
        # Click Search
        self.driver.find_element(*self.search_button).click()
        # Wait for employee result
        employee_result = (By.XPATH,f"//div[text()='{employee_name}']")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(employee_result))
        # Click employee
        self.driver.find_element(*employee_result).click()
        # Wait for Personal Details page
        WebDriverWait(self.driver, 10).until( EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Personal Details']")))
        # Chaining
        return PersonalDetailsPage(self.driver)